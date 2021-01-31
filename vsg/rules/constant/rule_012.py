
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rules import utils as rule_utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.constant_keyword, token.constant_declaration.semicolon])


class rule_012(rule.Rule):
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
        rule.Rule.__init__(self, 'constant', '012')
        self.solution = 'Align one space after assignment operator'
        self.phase = 5
        self.subphase = 4
        self.lTokenPairs = lTokenPairs
        self.bExcludeLastToken = False
        self.first_paren_new_line = False
        self.configuration.append('first_paren_new_line')
        self.last_paren_new_line = False
        self.configuration.append('last_paren_new_line')
        self.open_paren_new_line = False
        self.configuration.append('open_paren_new_line')
        self.close_paren_new_line = False
        self.configuration.append('close_paren_new_line')
        self.new_line_after_comma = False
        self.configuration.append('new_line_after_comma')
        self.align_left = True
        self.configuration.append('align_left')
        self.Ignore_single_line = True
        self.configuration.append('Ignore_single_line')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi


    def analyze(self, oFile):
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:

            if rule_utils.is_single_line(oToi) and self.Ignore_single_line:
                continue

            if not _is_open_paren_after_assignment(oToi):
                continue

            _check_first_paren_new_line(self, oToi)
            _check_last_paren_new_line(self, oToi)
            _check_open_paren_new_line(self, oToi)
            _check_close_paren_new_line(self, oToi)


#        for oNewToi in lToi:
#
#            iLine, lTokens = utils.get_toi_parameters(oNewToi)
#
#            bSearchOpen = False
#            bSearchClose = False
#            for iToken, oToken in enumerate(lTokens):
#                if isinstance(oToken, token.constant_declaration.assignment_operator):
#                    if utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis], iToken + 1, lTokens):
#                        bSearchOpen = True
#                if bSearchOpen:
#                    if isinstance(oToken, parser.open_parenthesis):
#                        iStartIndex = iToken
#                        bSearchOpen = False
#                        bSearchClose = True
#                if bSearchClose:
#                    if isinstance(oToken, parser.close_parenthesis):
#                        iEndIndex = iToken
#                if bSearchClose and isinstance(oToken, token.constant_declaration.semicolon):
#                    lNewTokens = lTokens.copy()
#                    lNewTokens = utils.remove_trailing_whitespace_and_comments(lNewTokens[:iEndIndex])
#                    iEndIndex = iEndIndex - ( len(lTokens) - len(lNewTokens) )
#                    oToi = oNewToi.extract_tokens(iStartIndex, iEndIndex)
#                    break
#            else:
#                continue
#
#            iLine, lTokens = utils.get_toi_parameters(oToi)
#
##            print('-'*80)
##            print(iLine)
##            print(lTokens)
#            iStartColumn = calculate_start_column(oFile, oToi)
#            lColumn = []
#            lColumn.append(iStartColumn)
#            bCheckAlignment = False
#            iFirstColumn = oFile.get_column_of_token_index(oToi.get_start_index())
#            iColumn = iFirstColumn
#            iPreviousColumn = 0
#            iIndent = 0
##            print('-'*80)
#            for iToken, oToken in enumerate(lTokens):
#
#                iLine = utils.increment_line_number(iLine, oToken)
#
#                if isinstance(oToken, parser.carriage_return):
#                    bCheckAlignment = True
#                    iPreviousColumn = lColumn[-1]
#                    iColumn = 0
#                    if isinstance(lTokens[iToken + 1], parser.whitespace):
#                        iIndent = len(lTokens[iToken + 1].get_value())
#                    else:
#                        iIndent = 0
#                    continue
#
#                if isinstance(oToken, parser.blank_line):
#                    bCheckAlignment = False
#                    continue
#
#                iColumn += len(oToken.get_value())
#
#                if isinstance(oToken, parser.open_parenthesis):
#                    lColumn.append(iColumn + iPreviousColumn - iIndent)
#
#                if isinstance(oToken, parser.close_parenthesis):
#                    lColumn.pop()
#
#                if bCheckAlignment:
#                    if isinstance(oToken, parser.whitespace):
#                        if len(oToken.get_value()) != lColumn[-1]:
#                            dAction = {}
#                            dAction['line'] = iLine
#                            dAction['column'] = lColumn[-1]
#                            dAction['action'] = 'adjust'
#                            dAction['indent'] = iIndent
#                            dAction['previous'] = iPreviousColumn
#                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), self.solution)
#                            oViolation.set_action(dAction)
#                            self.add_violation(oViolation)
##                            print(dAction)
#                    else:
#                        if lColumn != 0:
#                            dAction = {}
#                            dAction['line'] = iLine
#                            if isinstance(oToken, parser.open_parenthesis):
#                                dAction['column'] = lColumn[-2]
#                            else:
#                                dAction['column'] = lColumn[-1]
#                            dAction['action'] = 'insert'
#                            dAction['indent'] = iIndent
#                            dAction['previous'] = iPreviousColumn
#                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), self.solution)
#                            oViolation.set_action(dAction)
#                            self.add_violation(oViolation)
#                    bCheckAlignment = False
#
#    def _fix_violation(self, oViolation):
#        lTokens = oViolation.get_tokens()
#        dAction = oViolation.get_action()
#
#        if dAction['action'] == 'adjust':
#            lTokens[0].set_value(' '*dAction['column'])
#        else:
#            lTokens.insert(0, parser.whitespace(' '*dAction['column']))
#
#        oViolation.set_tokens(lTokens)


#def calculate_start_column(oFile, oToi):
#    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
#    iReturn += len(oToi.get_tokens()[0].get_value())
#    iReturn += 1
#    return iReturn


def _check_first_paren_new_line(self, oToi):
    
    if self.first_paren_new_line == 'Ignore':
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
                if self.first_paren_new_line:
                    sSolution = 'Move parenthesis after assignment to the next line.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iStart, iToken), sSolution)
                    self.add_violation(oViolation)
            else:
                if not self.first_paren_new_line:
                    sSolution = 'Move parenthesis to same line as assignment operator.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iStart, iToken), sSolution)
                    self.add_violation(oViolation)
            break
                
def _check_last_paren_new_line(self, oToi):
    if self.last_paren_new_line == 'Ignore':
        return 
    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    lTokens.reverse()
    iLine = iLine + utils.count_carriage_returns(lTokens)
    bReturnFound = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.decrement_line_number(iLine, oToken)
        if isinstance(oToken, parser.close_parenthesis):
            iEnd = len(lTokens) - iToken
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iToken + 1, lTokens):
                iStart = len(lTokens) - iToken - 2
                bReturnFound = True
            elif utils.are_next_consecutive_token_types([parser.carriage_return], iToken + 1, lTokens):
                iStart = len(lTokens) - iToken - 1
                bReturnFound = True
            
            if self.last_paren_new_line and not bReturnFound:
                lTokens.reverse()
                sSolution = 'Move closing parenthesis to the next line.'
                oViolation = violation.New(iLine, oToi.extract_tokens(iEnd, iEnd), sSolution)
                self.add_violation(oViolation)
            elif not self.last_paren_new_line and bReturnFound:
                lTokens.reverse()
                sSolution = 'Move closing parenthesis to previous line.'
                oViolation = violation.New(iLine, oToi.extract_tokens(iStart, iEnd), sSolution)
                self.add_violation(oViolation)

            break
                

def _check_open_paren_new_line(self, oToi):
    
    if self.open_paren_new_line == 'Ignore':
        return 

    iLine, lTokens = utils.get_toi_parameters(oToi)

    bSearch = False
    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            bSearch = True
        if isinstance(oToken, parser.open_parenthesis) and bSearch:
            if utils.is_token_at_end_of_line(iToken, lTokens):
                if not self.open_paren_new_line:
                    iEnd = utils.find_carriage_return(lTokens, iToken)
                    sSolution = 'Remove carriage return after open parenthesis.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iEnd), sSolution)
                    self.add_violation(oViolation)
            else:
                if self.open_paren_new_line:
                    sSolution = 'Add carriage return after open parenthesis.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                    self.add_violation(oViolation)
                

def _check_close_paren_new_line(self, oToi):
    if self.close_paren_new_line == 'Ignore':
        return 

    iLine, lTokens = utils.get_toi_parameters(oToi)
    bSearch = False
    for iToken, oToken in reversed(list(enumerate(lTokens))):
        if isinstance(oToken, parser.close_parenthesis):
            iEnd = iToken
            break

    bSearch = False
    for iToken, oToken in enumerate(lTokens[:iEnd]):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            bSearch = True
        if isinstance(oToken, parser.close_parenthesis) and bSearch:
            if utils.does_token_start_line(iToken, lTokens):
                if not self.close_paren_new_line:
                    sSolution = 'Move closing parenthesis to previous line.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                    self.add_violation(oViolation)
            else:
                if self.close_paren_new_line:
                    sSolution = 'Move closing parenthesis to the next line.'
                    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                    self.add_violation(oViolation)

  
def _is_open_paren_after_assignment(oToi):
    
    iLine, lTokens = utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, token.constant_declaration.assignment_operator):
            if utils.are_next_consecutive_token_types_ignoring_whitespace([token.constant_declaration.assignment_operator, parser.open_parenthesis], iToken, lTokens):
                return True
    return False
