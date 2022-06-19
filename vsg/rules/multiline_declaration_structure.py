
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class multiline_declaration_structure(structure.Rule):
    '''
    This rule checks the structure of multiline constants that contain arrays.

    |configuring_multiline_structure_rules_link|

    .. NOTE:: The indenting of multiline array constants is handled by the rule `constant_012 <constant_rules.html#constant-012>`_.

    **Violation**

    .. code-block:: vhdl

       constant rom : romq_type := (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    '''

    def __init__(self, name, identifier, lTokenPairs):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = True

        self.first_paren_new_line = 'no'
        self.configuration.append('first_paren_new_line')
        self.last_paren_new_line = 'no'
        self.configuration.append('last_paren_new_line')
        self.open_paren_new_line = 'no'
        self.configuration.append('open_paren_new_line')
        self.close_paren_new_line = 'no'
        self.configuration.append('close_paren_new_line')
        self.new_line_after_comma = 'no'
        self.configuration.append('new_line_after_comma')
        self.assign_on_single_line = 'no'
#        self.configuration.append('assign_on_single_line')
        self.ignore_single_line = 'yes'
        self.configuration.append('ignore_single_line')
        self.move_last_comment = 'ignore'
        self.configuration.append('move_last_comment')
        self.array_first_paren_new_line = 'ignore'
        self.configuration.append('array_first_paren_new_line')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken, bIncludeTillEndOfLine=True)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
#            print('='*80)
            if rules_utils.is_single_line(oToi) and self.ignore_single_line == 'yes':
                continue

            if not _is_record_type(oToi):
                continue

            _check_array_first_paren_new_line(self, oToi)
            _check_first_paren_new_line(self, oToi)
            _check_last_paren_new_line(self, oToi)
            _check_open_paren_new_line(self, oToi)
            _check_close_paren_new_line(self, oToi)
            _check_new_line_after_comma(self, oToi)
#            _check_assign_on_single_line(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction['type'] == 'first_paren_new_line':
            _fix_first_paren_new_line(oViolation)
        elif dAction['type'] == 'last_paren_new_line':
            _fix_last_paren_new_line(oViolation)
        elif dAction['type'] == 'open_paren_new_line':
            _fix_open_paren_new_line(oViolation)
        elif dAction['type'] == 'close_paren_new_line':
            _fix_close_paren_new_line(oViolation)
        elif dAction['type'] == 'new_line_after_comma':
            _fix_new_line_after_comma(oViolation)
        elif dAction['type'] == 'assign_on_single_line':
            _fix_assign_on_single_line(oViolation)
        elif dAction['type'] == 'array_first_paren_new_line':
            _fix_array_first_paren_new_line(oViolation)


def _check_array_first_paren_new_line(self, oToi):

    if self.array_first_paren_new_line == 'ignore':
        return

    iToken, iLine, iStopIndex, lTokens = extract_analysis_parameters(oToi)

    while iToken < iStopIndex:
#        print(f'==> iLine = {iLine} | iToken = {iToken}')
        oToken = lTokens[iToken]
        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.open_parenthesis):
#            print('---> Open paren detected')
            if is_array(iToken, lTokens):
#                print(f'Array @{iLine}')
                iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
                iLine += rules_utils.number_of_carriage_returns(lTokens[iToken:iToken])
                if utils.find_carriage_return(lTokens[iStart:iToken]) is None:
                    if self.array_first_paren_new_line == 'yes':
                        sSolution = 'Move parenthesis after assignment to the next line.'
                        oViolation = _create_violation(oToi, iLine, iToken, iToken, 'array_first_paren_new_line', 'insert', sSolution)
                        self.add_violation(oViolation)
                else:
                    if self.array_first_paren_new_line == 'no':
                        sSolution = 'Move parenthesis to same line as assignment operator.'
                        oViolation = _create_violation(oToi, iLine, iStart, iToken, 'array_first_paren_new_line', 'remove', sSolution)
                        self.add_violation(oViolation)
                iNextToken = find_index_of_matching_close_paren(iToken, lTokens) + 1
#                utils.print_lines(lTokens[iToken:iNextToken + 1])
                iToken = iNextToken
            else:
                iToken += 1
        else:
            iToken += 1


def extract_analysis_parameters(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)
    # Find the colon to setup next loop
    iToken = 0
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.signal_declaration.colon):
            break
    # Assign next loop parameters
    iToken += 1
    iStopIndex = len(lTokens)

    return iToken, iLine, iStopIndex, lTokens


def _check_first_paren_new_line(self, oToi):

    if self.first_paren_new_line == 'ignore':
        return

    iToken, iLine, iStopIndex, lTokens = extract_analysis_parameters(oToi)

    while iToken < iStopIndex:
#        print(f'==> iLine = {iLine} | iToken = {iToken}')
        oToken = lTokens[iToken]
        iLine = utils.increment_line_number(iLine, oToken)

        if isinstance(oToken, parser.open_parenthesis):
#            print('---> Open paren detected')
            if is_array(iToken, lTokens):
                iNextToken = find_index_of_matching_close_paren(iToken, lTokens) + 1
                iNextToken = utils.find_next_non_whitespace_token(iNextToken, lTokens)
                iLine += rules_utils.number_of_carriage_returns(lTokens[iToken:iNextToken])
                if isinstance(lTokens[iNextToken], parser.open_parenthesis):
#                    print(f'Array @{iLine}')
                    iStart = utils.find_previous_non_whitespace_token(iNextToken - 1, lTokens)
                    if utils.find_carriage_return(lTokens[iStart:iNextToken]) is None:
                        if self.first_paren_new_line == 'yes':
                            sSolution = 'Move parenthesis after assignment to the next line.'
                            oViolation = _create_violation(oToi, iLine, iNextToken, iNextToken, 'first_paren_new_line', 'insert', sSolution)
                            self.add_violation(oViolation)
                    else:
                        if self.first_paren_new_line == 'no':
                            sSolution = 'Move parenthesis to same line as assignment operator.'
                            oViolation = _create_violation(oToi, iLine, iStart, iNextToken, 'first_paren_new_line', 'remove', sSolution)
                            self.add_violation(oViolation)
#                    utils.print_lines(lTokens[iToken:iNextToken + 1])
                iToken = iNextToken
            else:
                iToken += 1
        else:
            iToken += 1


def is_array(iToken, lTokens):
#    print(oToken.iId)
#    print(f'upper_bounds = {lTokens[iToken + 1].get_value()}')
    iMatchingCloseParen = find_index_of_matching_close_paren(iToken, lTokens)
#    print(iMatchingCloseParen)
#    print(lTokens[iMatchingCloseParen].iId)
#    print(lTokens[iToken:iMatchingCloseParen + 1])
    iNextToken = utils.find_next_non_whitespace_token(iMatchingCloseParen + 1, lTokens)
#    print(lTokens[iNextToken])
    if utils.token_is_open_parenthesis(iNextToken, lTokens):
        return True
    return False

def find_index_of_matching_close_paren(iToken, lTokens):
    iParenId = lTokens[iToken].iId
    for iIndex in range(iToken + 1, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.close_parenthesis):
            if iParenId == lTokens[iIndex].iId:
                return iIndex
    return None


def __check_first_paren_new_line(self, oToi):

    if self.first_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.signal_declaration.colon):
            bSearch = True
            continue
        if isinstance(oToken, parser.open_parenthesis) and bSearch:
            iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
            if utils.find_carriage_return(lTokens[iStart:iToken]) is None:
                if self.first_paren_new_line == 'yes':
                    sSolution = 'Move parenthesis after assignment to the next line.'
                    oViolation = _create_violation(oToi, iLine, iToken, iToken, 'first_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.first_paren_new_line == 'no':
                    sSolution = 'Move parenthesis to same line as assignment operator.'
                    oViolation = _create_violation(oToi, iLine, iStart, iToken, 'first_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            break


def _check_last_paren_new_line(self, oToi):

    if self.last_paren_new_line == 'ignore':
        return
    iLine, lTokens = utils.get_toi_parameters(oToi)
    lTokens.reverse()
    iLine = iLine + utils.count_carriage_returns(lTokens)
    bReturnFound = False
    bCommentFound = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.decrement_line_number(iLine, oToken)
        if isinstance(oToken, parser.comment):
            bCommentFound = True
        if isinstance(oToken, parser.close_parenthesis):
            iEnd = len(lTokens) - iToken - 1
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iToken + 1, lTokens):
                bReturnFound = True
            elif utils.are_next_consecutive_token_types([parser.carriage_return], iToken + 1, lTokens):
                bReturnFound = True

            lTokens.reverse()

            if self.last_paren_new_line == 'yes' and not bReturnFound:
                if self.move_last_comment == 'yes' and bCommentFound:
                    sSolution = 'Move parenthesis after assignment to the next line and trailing comment to previous line.'
                    oViolation = _create_violation(oToi, iLine, iEnd - 1, len(lTokens) - 1, 'last_paren_new_line', 'insert_and_move_comment', sSolution)
                    self.add_violation(oViolation)
                else:
                    sSolution = 'Move closing parenthesis to the next line.'
                    oViolation = _create_violation(oToi, iLine, iEnd - 1, iEnd, 'last_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)
            elif self.last_paren_new_line == 'no' and bReturnFound:
                sSolution = 'Move closing parenthesis to previous line.'
                iStart = utils.find_previous_non_whitespace_token(iEnd - 1, lTokens)
                oViolation = _create_violation(oToi, iLine, iStart, iEnd, 'last_paren_new_line', 'remove', sSolution)
                self.add_violation(oViolation)

            break


def _check_open_paren_new_line(self, oToi):

    if self.open_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    iStartIndex = _find_colon(lTokens) + 1
    bFirstParenFound = False
    for iToken in range(iStartIndex, len(lTokens)):

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            if bFirstParenFound:
               iPreviousIndex = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
               if something(iPreviousIndex, lTokens):
                   continue
            bFirstParenFound = True
            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.open_paren_new_line == 'no':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Remove carriage return after open parenthesis.'
                    oViolation = _create_violation(oToi, iErrorLine, iToken, iEnd, 'open_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.open_paren_new_line == 'yes':
                    sSolution = 'Add carriage return after open parenthesis.'
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    oViolation = _create_violation(oToi, iErrorLine, iToken, iToken, 'open_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)


def something(iToken, lTokens):
#    print('--> Something')
#    print(lTokens[iToken].get_value())
    if utils.token_is_open_parenthesis(iToken, lTokens):
        return False
    if utils.token_is_comma(iToken, lTokens):
        return False
    return True


def something_else(iToken, lTokens):
    if utils.token_is_close_parenthesis(iToken, lTokens):
        return False
    return True


def _check_close_paren_new_line(self, oToi):

    if self.close_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

#    iToken = _find_colon(lTokens) + 1
#    iStopIndex = _find_last_closing_paren(lTokens)
    bFirstParenFound = False
    for iToken in range(_find_colon(lTokens) + 1, _find_last_closing_paren(lTokens)):
#    while iToken < iStopIndex:

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        if isinstance(oToken, parser.close_parenthesis):
            if bFirstParenFound:
                iPreviousIndex = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
                if something_else(iPreviousIndex, lTokens):
                    continue
            if utils.does_token_start_line(iToken, lTokens):
                if self.close_paren_new_line == 'no':
                    iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Move closing parenthesis to previous line.'
                    oViolation = _create_violation(oToi, iErrorLine, iStart, iToken, 'close_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.close_paren_new_line == 'yes':
                    iStart = iToken - 1
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Move closing parenthesis to the next line.'
                    oViolation = _create_violation(oToi, iErrorLine, iStart, iToken, 'close_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)


def _check_new_line_after_comma(self, oToi):

    if self.new_line_after_comma == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False
    bPositionalFound = True

    iToken = _find_colon(lTokens) + 1
    iStopIndex = len(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)

            if bOthersClause:
                bPositionalFound = True
                iToken += 1
                continue

            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bAssignmentFound:
               iToken += 1
               bPositionalFound = False
               continue

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        if isinstance(oToken, parser.comma):
            if bPositionalFound and self.new_line_after_comma == 'ignore_positional':
                iToken += 1
                bPositionalFound = True
                continue

            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.new_line_after_comma == 'no':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Remove carriage return after comma.'
                    oViolation = _create_violation(oToi, iErrorLine, iToken, iEnd, 'new_line_after_comma', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.new_line_after_comma == 'yes' or self.new_line_after_comma == 'ignore_positional':
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Add carriage return after comma.'
                    oViolation = _create_violation(oToi, iErrorLine, iToken, iToken + 1, 'new_line_after_comma', 'insert', sSolution)
                    self.add_violation(oViolation)

        iToken += 1

    return None


def _check_assign_on_single_line(self, oToi):

    if self.assign_on_single_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False

    iToken = _find_colon(lTokens) + 1
    iStopIndex = len(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)

            if bOthersClause:
                iToken += 1
                continue

            if lTokens[iToken].get_value() == ':':
                iPreviousToken = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bAssignmentFound:
#                rules_utils.print_debug(lTokens[iPreviousToken:iToken + 1])
                if rules_utils.number_of_carriage_returns(lTokens[iPreviousToken:iToken]) > 0:
                     iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iPreviousToken]) + iLine
                     sSolution = 'Remove carriage returns for assignments.'
                     oViolation = _create_violation(oToi, iErrorLine, iPreviousToken, iToken, 'assign_on_single_line', 'remove', sSolution)
                     self.add_violation(oViolation)


        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        iToken += 1

    return None


def _is_record_type(oToi):

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.signal_declaration.colon):
            if utils.find_in_range(',', iToken, ';', lTokens):
                return something_else_else(lTokens[iToken:])
    return False


def something_else_else(lTokens):
    bInsideFunction = False
    for iToken, oToken in enumerate(lTokens):
#        print(oToken.get_value())
#        print(bInsideFunction)
        if utils.token_is_open_parenthesis(iToken, lTokens):
           iPreviousIndex = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
           if something(iPreviousIndex, lTokens):
               bInsideFunction = True
        if utils.token_is_close_parenthesis(iToken, lTokens):
            bInsideFunction = False
#        print(f'{oToken.get_value()} | {bInsideFunction}')
        if utils.token_is_comma(iToken, lTokens) and not bInsideFunction:
            return True
    return False


def _fix_array_first_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 0)
        rules_utils.insert_carriage_return(lTokens, 0)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_first_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 0)
        rules_utils.insert_carriage_return(lTokens, 0)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        rules_utils.append_whitespace(lNewTokens)
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_last_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 1)
        rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)
    elif dAction['action'] == 'insert_and_move_comment':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 1)
        iSwapIndex = rules_utils.get_index_of_token_in_list(token.signal_declaration.semicolon, lTokens) + 1
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.extend(lTokens[iSwapIndex:])
        rules_utils.append_carriage_return(lNewTokens)
        lNewTokens.extend(lTokens[1:iSwapIndex])

        oViolation.set_tokens(lNewTokens)


def _fix_open_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        rules_utils.append_carriage_return(lTokens)
        rules_utils.append_whitespace(lTokens)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_close_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 1)
        rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_new_line_after_comma(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if isinstance(lTokens[1], parser.whitespace):
            rules_utils.insert_carriage_return(lTokens, 1)
        else:
            rules_utils.insert_whitespace(lTokens, 1)
            rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_assign_on_single_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    lNewTokens = []
    if dAction['action'] == 'remove':
        lNewTokens = utils.remove_carriage_returns_from_token_list(lTokens)
        lNewTokens = utils.remove_comments_from_token_list(lNewTokens)
        lNewTokens = utils.remove_consecutive_whitespace_tokens(lNewTokens)

        oViolation.set_tokens(lNewTokens)


def _inside_others_clause(iToken, lTokens):
    for oToken in lTokens[iToken + 1:]:
        if utils.token_is_whitespace_or_comment(oToken):
            continue
        elif isinstance(oToken, parser.open_parenthesis):
            return False
        elif isinstance(oToken, parser.close_parenthesis):
            return False
        else:
            if oToken.get_value().lower() == 'others':
                break
    else:
        return False
    return True


def _create_violation(oToi, iLine, iStartIndex, iEndIndex, sType, sAction, sSolution):
    dAction = _create_action_dictionary(sType, sAction)
    oViolation = violation.New(iLine, oToi.extract_tokens(iStartIndex, iEndIndex), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def _create_action_dictionary(sType, sAction):
    dReturn = {}
    dReturn['type'] = sType
    dReturn['action'] = sAction
    return dReturn


def _find_colon(lTokens):
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.signal_declaration.colon):
            return iToken
    return None


def _find_last_closing_paren(lTokens):
    iReturn = None
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.close_parenthesis):
            iReturn = iToken
    return iReturn


def _classify_assignment(iToken, lTokens):

    oToken = lTokens[iToken]
    if oToken.get_value() == '=>':
        iOpenParen = 0
        iCloseParen = 0
        for iReturn, oToken in enumerate(lTokens[iToken:]):
            if isinstance(oToken, parser.open_parenthesis):
                iOpenParen += 1
            elif isinstance(oToken, parser.close_parenthesis):
                iEnd = iToken + iReturn
                iCloseParen += 1
                if iCloseParen > iOpenParen:
#                    print(lTokens[iToken:iEnd -1])
#                    rules_utils.print_debug(lTokens[iToken:iEnd + 1])
                    iEnd = utils.find_previous_non_whitespace_token(iEnd - 1, lTokens)
                    return iEnd, True
                elif iOpenParen == iCloseParen:
#                    print(lTokens[iToken:iEnd])
#                    rules_utils.print_debug(lTokens[iToken:iEnd + 1])
                    return iEnd, True
            elif isinstance(oToken, parser.comma):
                if iOpenParen == iCloseParen:
                    iEnd = iToken + iReturn - 1
#                    print(lTokens[iToken:iEnd])
#                    rules_utils.print_debug(lTokens[iToken:iEnd + 1])
                    return iEnd, True
        return None
    return iToken, False


def _classify_others(iToken, lTokens):
    oToken = lTokens[iToken]
    if oToken.get_value() == '(':
        iOpenParen = 0
        iCloseParen = 0
        iStart = iToken
        for iReturn, oToken in enumerate(lTokens[iToken:]):
            if isinstance(oToken, parser.open_parenthesis):
                iOpenParen += 1
            elif isinstance(oToken, parser.close_parenthesis):
                iCloseParen += 1
                if iOpenParen == iCloseParen:
                    break
        else:
            return iToken, False

        iEnd = iReturn + iStart

        for iIndex in range(iStart + 1, iEnd):
            if lTokens[iIndex].get_value().lower() == 'others':
                return iEnd, True

    return iToken, False
