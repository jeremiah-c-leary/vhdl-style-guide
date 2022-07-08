
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class multiline_structure(structure.Rule):
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
        self.phase = 5
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = True

        self.first_paren_new_line = 'yes'
        self.configuration.append('first_paren_new_line')
        self.last_paren_new_line = 'yes'
        self.configuration.append('last_paren_new_line')
        self.open_paren_new_line = 'yes'
        self.configuration.append('open_paren_new_line')
        self.close_paren_new_line = 'yes'
        self.configuration.append('close_paren_new_line')
        self.new_line_after_comma = 'yes'
        self.configuration.append('new_line_after_comma')
        self.assign_on_single_line = 'yes'
        self.configuration.append('assign_on_single_line')
        self.ignore_single_line = 'yes'
        self.configuration.append('ignore_single_line')
        self.move_last_comment = 'ignore'
        self.configuration.append('move_last_comment')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken, bIncludeTillEndOfLine=True)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)

        lReturn = []
        for oToi in lToi:
            if rules_utils.is_single_line(oToi) and self.ignore_single_line:
                continue

            if not _is_open_paren_after_assignment(oToi):
                continue

            lReturn.append(oToi)

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:

            _check_first_paren_new_line(self, oToi)
            _check_last_paren_new_line(self, oToi)
            _check_open_paren_new_line(self, oToi)
            _check_close_paren_new_line(self, oToi)
            _check_new_line_after_comma(self, oToi)
            _check_assign_on_single_line(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        dAction['type'](oViolation)


def _check_first_paren_new_line(self, oToi):

    if self.first_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            iStart = iToken
            bSearch = True
        if isinstance(oToken, parser.open_parenthesis) and bSearch:
            if utils.find_carriage_return(lTokens[iStart:iToken]) is None:
                if self.first_paren_new_line == 'yes':
                    sSolution = 'Move parenthesis after assignment to the next line.'
                    oToi.set_meta_data('iLine', iLine)
                    oToi.set_meta_data('iStartIndex', iToken - 1)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_first_paren_new_line)
                    oToi.set_meta_data('sAction', 'insert')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
            else:
                if self.first_paren_new_line == 'no':
                    sSolution = 'Move parenthesis to same line as assignment operator.'
                    oToi.set_meta_data('iLine', iLine)
                    oToi.set_meta_data('iStartIndex', iStart)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_first_paren_new_line)
                    oToi.set_meta_data('sAction', 'remove')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
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
                    oToi.set_meta_data('iLine', iLine)
                    oToi.set_meta_data('iStartIndex', iEnd - 1)
                    oToi.set_meta_data('iEndIndex', len(lTokens) - 1)
                    oToi.set_meta_data('sType', _fix_last_paren_new_line)
                    oToi.set_meta_data('sAction', 'insert_and_move_comment')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
                else:
                    sSolution = 'Move closing parenthesis to the next line.'
                    oToi.set_meta_data('iLine', iLine)
                    oToi.set_meta_data('iStartIndex', iEnd - 1)
                    oToi.set_meta_data('iEndIndex', iEnd)
                    oToi.set_meta_data('sType', _fix_last_paren_new_line)
                    oToi.set_meta_data('sAction', 'insert')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
            elif self.last_paren_new_line == 'no' and bReturnFound:
                iStart = utils.find_previous_non_whitespace_token(iEnd - 1, lTokens)
                oToi.set_meta_data('iLine', iLine)
                oToi.set_meta_data('iStartIndex', iStart)
                oToi.set_meta_data('iEndIndex', iEnd)
                oToi.set_meta_data('sType', _fix_last_paren_new_line)
                oToi.set_meta_data('sAction', 'remove')
                oToi.set_meta_data('sSolution', 'Move closing parenthesis to previous line.')
                oViolation = _create_violation(oToi)
                self.add_violation(oViolation)

            break


def _check_open_paren_new_line(self, oToi):

    if self.open_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False

    iToken = _find_assignment_operator(lTokens) + 1
    iStopIndex = len(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)

            if bOthersClause:
                iToken += 1
                continue

            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bAssignmentFound:
                iToken += 1
                continue

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True
            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.open_paren_new_line == 'no':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Remove carriage return after open parenthesis.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iToken)
                    oToi.set_meta_data('iEndIndex', iEnd)
                    oToi.set_meta_data('sType', _fix_open_paren_new_line)
                    oToi.set_meta_data('sAction', 'remove')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
            else:
                if self.open_paren_new_line == 'yes':
                    sSolution = 'Add carriage return after open parenthesis.'
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iToken)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_open_paren_new_line)
                    oToi.set_meta_data('sAction', 'insert')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
        bOthersClause = False
        iToken += 1

    return None


def _check_close_paren_new_line(self, oToi):

    if self.close_paren_new_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False

    iToken = _find_assignment_operator(lTokens) + 1
    iStopIndex = _find_last_closing_paren(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)

            if bOthersClause:
                iToken += 1
                continue

            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bAssignmentFound:
                iToken += 1
                continue

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        if isinstance(oToken, parser.close_parenthesis):
            if utils.does_token_start_line(iToken, lTokens):
                if self.close_paren_new_line == 'no':
                    iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Move closing parenthesis to previous line.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iStart)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_close_paren_new_line)
                    oToi.set_meta_data('sAction', 'remove')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
            else:
                if self.close_paren_new_line == 'yes':
                    iStart = iToken - 1
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Move closing parenthesis to the next line.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iStart)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_close_paren_new_line)
                    oToi.set_meta_data('sAction', 'insert')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)

        iToken += 1

    return None


def _check_new_line_after_comma(self, oToi):

    if self.new_line_after_comma == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False
    bPositionalFound = True

    iToken = _find_assignment_operator(lTokens) + 1
    iStopIndex = len(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)
            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bOthersClause:
                bPositionalFound = True
                iToken += 1

            if bAssignmentFound:
                iToken += 1
                bPositionalFound = False

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        if isinstance(oToken, parser.comma):
            if bPositionalFound and self.new_line_after_comma == 'ignore_positional':
                iToken += 1
                continue

            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.new_line_after_comma == 'no':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Remove carriage return after comma.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iToken)
                    oToi.set_meta_data('iEndIndex', iEnd)
                    oToi.set_meta_data('sType', _fix_new_line_after_comma)
                    oToi.set_meta_data('sAction', 'remove')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)
            else:
                if self.new_line_after_comma == 'yes' or self.new_line_after_comma == 'ignore_positional':
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iToken]) + iLine
                    sSolution = 'Add carriage return after comma.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iToken)
                    oToi.set_meta_data('iEndIndex', iToken + 1)
                    oToi.set_meta_data('sType', _fix_new_line_after_comma)
                    oToi.set_meta_data('sAction', 'insert')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)

        iToken += 1

    return None


def _check_assign_on_single_line(self, oToi):

    if self.assign_on_single_line == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bAssignmentFound = False
    bOthersClause = False

    iToken = _find_assignment_operator(lTokens) + 1
    iStopIndex = len(lTokens)
    bFirstParenFound = False
    while iToken < iStopIndex:

        if bFirstParenFound:
            iToken, bOthersClause = _classify_others(iToken, lTokens)

            if bOthersClause:
                iToken += 1
                continue

            if lTokens[iToken].get_value() == '=>':
                iPreviousToken = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
            iToken, bAssignmentFound = _classify_assignment(iToken, lTokens)

            if bAssignmentFound:
                if rules_utils.number_of_carriage_returns(lTokens[iPreviousToken:iToken]) > 0:
                    iErrorLine = rules_utils.number_of_carriage_returns(lTokens[:iPreviousToken]) + iLine
                    sSolution = 'Remove carriage returns for assignments.'
                    oToi.set_meta_data('iLine', iErrorLine)
                    oToi.set_meta_data('iStartIndex', iPreviousToken)
                    oToi.set_meta_data('iEndIndex', iToken)
                    oToi.set_meta_data('sType', _fix_assign_on_single_line)
                    oToi.set_meta_data('sAction', 'remove')
                    oToi.set_meta_data('sSolution', sSolution)
                    oViolation = _create_violation(oToi)
                    self.add_violation(oViolation)

        oToken = lTokens[iToken]

        if isinstance(oToken, parser.open_parenthesis):
            bFirstParenFound = True

        iToken += 1

    return None


def _is_open_paren_after_assignment(oToi):

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            lExpectedTokens = [token.constant_declaration.assignment_operator, parser.open_parenthesis]
            if utils.are_next_consecutive_token_types_ignoring_whitespace(lExpectedTokens, iToken, lTokens):
                return True
    return False


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
        iSwapIndex = rules_utils.get_index_of_token_in_list(token.constant_declaration.semicolon, lTokens) + 1
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
        elif rules_utils.token_is_parenthesis(oToken):
            return False
        else:
            if oToken.get_value().lower() == 'others':
                break
    else:
        return False
    return True


def _create_violation(oToi):
    iLine = oToi.get_meta_data('iLine')
    iStartIndex = oToi.get_meta_data('iStartIndex')
    iEndIndex = oToi.get_meta_data('iEndIndex')
    sType = oToi.get_meta_data('sType')
    sAction = oToi.get_meta_data('sAction')
    sSolution = oToi.get_meta_data('sSolution')
    dAction = _create_action_dictionary(sType, sAction)
    oViolation = violation.New(iLine, oToi.extract_tokens(iStartIndex, iEndIndex), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def _create_action_dictionary(sType, sAction):
    dReturn = {}
    dReturn['type'] = sType
    dReturn['action'] = sAction
    return dReturn


def _found_assignment_operator(oToken, bSearch):
    if bSearch:
        return True
    if isinstance(oToken, token.constant_declaration.assignment_operator):
        return True
    return False


def _find_assignment_operator(lTokens):
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.constant_declaration.assignment_operator):
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
            iOpenParen = rules_utils.update_open_paren_counter(oToken, iOpenParen)
            iCloseParen = rules_utils.update_close_paren_counter(oToken, iCloseParen)
            iEnd = iToken + iReturn
            if something(oToken, iOpenParen, iCloseParen):
                iEnd = utils.find_previous_non_whitespace_token(iEnd - 1, lTokens)
                return iEnd, True
            if something_else(oToken, iOpenParen, iCloseParen):
                return iEnd, True
            if other_thing(oToken, iOpenParen, iCloseParen):
                iEnd = iToken + iReturn - 1
                return iEnd, True
        return None
    return iToken, False


def other_thing(oToken, iOpenParen, iCloseParen):
    if isinstance(oToken, parser.comma) and iOpenParen == iCloseParen:
        return True
    return False


def something_else(oToken, iOpenParen, iCloseParen):
    if isinstance(oToken, parser.close_parenthesis) and iCloseParen == iOpenParen:
            return True
    return False


def something(oToken, iOpenParen, iCloseParen):
    if isinstance(oToken, parser.close_parenthesis) and iCloseParen > iOpenParen:
            return True
    return False


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
