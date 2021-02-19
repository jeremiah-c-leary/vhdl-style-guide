
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rules import utils as rule_utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.constant_keyword, token.constant_declaration.semicolon])


class rule_016(rule.Rule):
    '''
    Checks for the proper indentation of multiline constants.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'constant', '016')
        self.solution = 'Align one space after assignment operator'
        self.phase = 1
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = False

        self.first_paren_new_line = 'false'
        self.configuration.append('first_paren_new_line')
        self.last_paren_new_line = 'false'
        self.configuration.append('last_paren_new_line')
        self.open_paren_new_line = 'false'
        self.configuration.append('open_paren_new_line')
        self.close_paren_new_line = 'false'
        self.configuration.append('close_paren_new_line')
        self.new_line_after_comma = 'false'
        self.configuration.append('new_line_after_comma')
        self.ignore_single_line = 'false'
        self.configuration.append('ignore_single_line')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            if rule_utils.is_single_line(oToi) and self.ignore_single_line:
                continue

            if not _is_open_paren_after_assignment(oToi):
                continue

            _check_first_paren_new_line(self, oToi)
            _check_last_paren_new_line(self, oToi)
            _check_open_paren_new_line(self, oToi)
            _check_close_paren_new_line(self, oToi)
            _check_new_line_after_comma(self, oToi)

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
                if self.first_paren_new_line == 'true':
                    sSolution = 'Move parenthesis after assignment to the next line.'
                    oViolation = _create_violation(oToi, iLine, iToken - 1, iToken, 'first_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.first_paren_new_line == 'false':
                    sSolution = 'Move parenthesis to same line as assignment operator.'
                    oViolation = _create_violation(oToi, iLine, iStart, iToken, 'first_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            break


def _check_last_paren_new_line(self, oToi):
#    print('-->_check_last_paren_new_line')    
    if self.last_paren_new_line == 'ignore':
        return 
    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    lTokens.reverse()
    iLine = iLine + utils.count_carriage_returns(lTokens)
    bReturnFound = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.decrement_line_number(iLine, oToken)
        if isinstance(oToken, parser.close_parenthesis):
            iEnd = len(lTokens) - iToken - 1
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iToken + 1, lTokens):
                bReturnFound = True
            elif utils.are_next_consecutive_token_types([parser.carriage_return], iToken + 1, lTokens):
                bReturnFound = True

            lTokens.reverse()            

            if self.last_paren_new_line == 'true' and not bReturnFound:
                sSolution = 'Move closing parenthesis to the next line.'
                oViolation = _create_violation(oToi, iLine, iEnd - 1, iEnd, 'last_paren_new_line', 'insert', sSolution)
                self.add_violation(oViolation)
            elif self.last_paren_new_line == 'false' and bReturnFound:
                sSolution = 'Move closing parenthesis to previous line.'
                iStart = utils.find_previous_non_whitespace_token(iEnd - 1, lTokens)
                oViolation = _create_violation(oToi, iLine, iStart, iEnd, 'last_paren_new_line', 'remove', sSolution)
                self.add_violation(oViolation)

            break
                

def _check_open_paren_new_line(self, oToi):
#    print('-->_check_open_paren_new_line')    
    
    if self.open_paren_new_line == 'ignore':
        return 

    iLine, lTokens = utils.get_toi_parameters(oToi)
#    print(lTokens)

    bSearch = False
    iOpenParen = 0
    iCloseParen = 0
    bAssignmentFound = False
    bOthersClause = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            bSearch = True
        if not bSearch:
            continue


        if isinstance(oToken, parser.close_parenthesis):
            if bOthersClause:
                bOthersClause = False
                continue

        if isinstance(oToken, parser.open_parenthesis):
#            print(f'_check_open_paren_new_line = {_inside_others_clause(iToken, lTokens)}')
            if _inside_others_clause(iToken, lTokens):
                bOthersClause = True

        if bOthersClause:
            continue



        if bAssignmentFound:
            if isinstance(oToken, parser.close_parenthesis):
                iCloseParen += 1
                if iOpenParen == iCloseParen:
                    bAssignmentFound = False
                elif iCloseParen > iOpenParen:
                    bAssignmentFound = False
    
            if isinstance(oToken, parser.open_parenthesis):
                iOpenParen += 1

            continue

        if not bAssignmentFound and oToken.get_value() == '=>':
            bAssignmentFound = True
            iOpenParen = 0
            iCloseParen = 0
            continue

        if isinstance(oToken, parser.open_parenthesis):
            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.open_paren_new_line == 'false':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    sSolution = 'Remove carriage return after open parenthesis.'
                    oViolation = _create_violation(oToi, iLine, iToken, iEnd, 'open_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.open_paren_new_line == 'true':
                    sSolution = 'Add carriage return after open parenthesis.'
                    oViolation = _create_violation(oToi, iLine, iToken, iToken, 'open_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)
                

def _check_close_paren_new_line(self, oToi):
#    print('-->_check_close_paren_new_line')    
    if self.close_paren_new_line == 'ignore':
        return 

    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    for iToken, oToken in reversed(list(enumerate(lTokens))):
        if isinstance(oToken, parser.close_parenthesis):
            iEnd = iToken
            break

    bSearch = False
    iOpenParen = 0
    iCloseParen = 0
    bAssignmentFound = False
    bOthersClause = False
    for iToken, oToken in enumerate(lTokens[:iEnd]):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            bSearch = True
        if not bSearch:
            continue

        if isinstance(oToken, parser.close_parenthesis):
            if bOthersClause:
                iCloseParen += 1
#                if iOpenParen == iCloseParen:
#                    bOthersClause = False
#                    continue
#                elif iCloseParen > iOpenParen:
                if iCloseParen > iOpenParen:
                    bOthersCluase = False

        if isinstance(oToken, parser.open_parenthesis):
            if not bOthersClause:
#            print(f'_check_new_line_after_comma = {_inside_others_clause(iToken, lTokens)}')
                if _inside_others_clause(iToken, lTokens):
                    bOthersClause = True
                    iOpenParen = 0
                    iCloseParen = 0
            else:
                iOpenParen += 1

        if bOthersClause:
            continue


        if bAssignmentFound:
            if isinstance(oToken, parser.close_parenthesis):
                iCloseParen += 1
                if iOpenParen == iCloseParen:
                    bAssignmentFound = False
                    continue
                elif iCloseParen > iOpenParen:
                    bAssignmentFound = False 
                else:
                    continue

            elif isinstance(oToken, parser.open_parenthesis):
                iOpenParen += 1
                continue

            elif isinstance(oToken, parser.comma):
                if iOpenParen == iCloseParen:
                    bAssignmentFound = False
                else:
                    continue
            else:
                continue

        if not bAssignmentFound and oToken.get_value() == '=>':
            bAssignmentFound = True
            iOpenParen = 0
            iCloseParen = 0
            continue

        if isinstance(oToken, parser.close_parenthesis):
            if utils.does_token_start_line(iToken, lTokens):
                if self.close_paren_new_line == 'false':
                    iStart = utils.find_previous_non_whitespace_token(iToken - 1, lTokens)
                    sSolution = 'Move closing parenthesis to previous line.'
                    oViolation = _create_violation(oToi, iLine, iStart, iToken, 'close_paren_new_line', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.close_paren_new_line == 'true':
                    sSolution = 'Move closing parenthesis to the next line.'
                    oViolation = _create_violation(oToi, iLine, iToken - 1, iToken, 'close_paren_new_line', 'insert', sSolution)
                    self.add_violation(oViolation)


def _check_new_line_after_comma(self, oToi):
#    print('-->_check_new_line_after_comma')    
    
    if self.new_line_after_comma == 'ignore':
        return 

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bSearch = False
    iOpenParen = 0
    iCloseParen = 0
    bAssignmentFound = False
    bOthersClause = False
    bPositionalFound = True
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            bSearch = True
        if not bSearch:
            continue

        if isinstance(oToken, parser.close_parenthesis):
            if bOthersClause:
                iCloseParen += 1
#                if iOpenParen == iCloseParen:
#                    bOthersClause = False
#                    continue
#                elif iCloseParen > iOpenParen:
                if iCloseParen > iOpenParen:
                    bOthersClause = False

        if isinstance(oToken, parser.open_parenthesis):
            if not bOthersClause:
#            print(f'_check_new_line_after_comma = {_inside_others_clause(iToken, lTokens)}')
                if _inside_others_clause(iToken, lTokens):
                    bOthersClause = True
                    bPositionalFound = True
                    iOpenParen = 0
                    iCloseParen = 0
            else:
                iOpenParen += 1

        if bOthersClause:
            continue

        if bAssignmentFound:
            if isinstance(oToken, parser.close_parenthesis):
                iCloseParen += 1
                if iOpenParen == iCloseParen:
                    bAssignmentFound = False
                elif iCloseParen > iOpenParen:
                    bAssignmentFound = False
    
            if isinstance(oToken, parser.open_parenthesis):
                iOpenParen += 1

            if isinstance(oToken, parser.comma):
                if iOpenParen == iCloseParen:
                    bAssignmentFound = False
                else:
                    continue
            else:
                continue

        if not bAssignmentFound and oToken.get_value() == '=>':
            bAssignmentFound = True
            iOpenParen = 0
            iCloseParen = 0
            bPositionalFound = False
            continue

        if isinstance(oToken, parser.comma):
            if bPositionalFound and self.new_line_after_comma == 'ignore_positional':
                continue
            bPositionalFound = True

            if utils.is_token_at_end_of_line(iToken, lTokens):
                if self.new_line_after_comma == 'false':
                    iEnd = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                    sSolution = 'Remove carriage return after comma.'
                    oViolation = _create_violation(oToi, iLine, iToken, iEnd, 'new_line_after_comma', 'remove', sSolution)
                    self.add_violation(oViolation)
            else:
                if self.new_line_after_comma == 'true' or self.new_line_after_comma == 'ignore_positional':
                    sSolution = 'Add carriage return after comma.'
                    oViolation = _create_violation(oToi, iLine, iToken, iToken + 1, 'new_line_after_comma', 'insert', sSolution)
                    self.add_violation(oViolation)
                
  
def _is_open_paren_after_assignment(oToi):
    
    iLine, lTokens = utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.constant_declaration.assignment_operator, parser.open_parenthesis], iToken, lTokens):
                return True
    return False


def _fix_first_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            lTokens.insert(0, parser.whitespace(' '))
        lTokens.insert(0, parser.carriage_return())
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_last_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            lTokens.insert(1, parser.whitespace(' '))
        lTokens.insert(1, parser.carriage_return())
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _fix_open_paren_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        lTokens.append(parser.carriage_return())
        lTokens.append(parser.whitespace(' '))
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
            lTokens.insert(1, parser.whitespace(' '))
        lTokens.insert(1, parser.carriage_return())
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
            lTokens.insert(1, parser.carriage_return())
        else:
            lTokens.insert(1, parser.whitespace(' '))
            lTokens.insert(1, parser.carriage_return())
#            lTokens.append(parser.carriage_return())
#            lTokens.append(parser.whitespace(' '))
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _inside_others_clause(iToken, lTokens):
#    print(lTokens[iToken + 1:])
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
