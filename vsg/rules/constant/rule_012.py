
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])

class rule_012(rule.Rule):
    '''
    Checks the case for words.

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
        self.solution = 'Align with open parenthesis on previous line.'
        self.phase = 4
        self.lTokenPairs = lTokenPairs
        self.align_left = False
        self.configuration.append('align_left')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def analyze(self, oFile):
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:

            print('-'*80)
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iStartColumn = calculate_start_column(oFile, oToi)
            lColumn = []
            lColumn.append(iStartColumn)
            bCheckAlignment = False
            iFirstColumn, iNextColumn = _find_first_column(oFile, oToi, self.align_left)
            iColumn = iFirstColumn
            iPreviousColumn = 0
            iIndent = 0
            bSkipPop = False
            bPopFirstColumn = True
            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.carriage_return):
                    print(lColumn)
                    if bPopFirstColumn and self.align_left:
                        lColumn = [iNextColumn]
                        bPopFirstColumn = False 
                    bCheckAlignment = True
                    iPreviousColumn = lColumn[-1]
                    iColumn = 0
                    if isinstance(lTokens[iToken + 1], parser.whitespace):
                        iIndent = len(lTokens[iToken + 1].get_value())
                        if isinstance(lTokens[iToken + 2], parser.close_parenthesis):
                            lColumn.pop()
                            print(f'Close Paren = {lColumn}')
                            bSkipPop = True

                    else:
                        iIndent = 0
                    continue

                if isinstance(oToken, parser.blank_line):
                    bCheckAlignment = False
                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, parser.close_parenthesis) and bSkipPop:
                    bSkipPop = False
                elif isinstance(oToken, parser.close_parenthesis):
                    lColumn.pop()
                    print(f'Close Paren = {lColumn}')

                if bCheckAlignment:
                    if isinstance(oToken, parser.whitespace):
                        if len(oToken.get_value()) != lColumn[-1]:
                            dAction = {}
                            dAction['line'] = iLine
                            dAction['column'] = lColumn[-1]
                            dAction['action'] = 'adjust'
                            sSolution = 'Adjust indent to column ' + str(iIndent + lColumn[-1])
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                            print(f"Action = {dAction['action']}")
#                            print(dAction)
                    else:
                        if lColumn != 0:
                            dAction = {}
                            dAction['line'] = iLine
                            dAction['column'] = lColumn[-1]
                            dAction['action'] = 'insert'
                            sSolution = 'Adjust indent to column ' + str(iIndent + lColumn[-1])
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                            print(f"Action = {dAction['action']}")
                    bCheckAlignment = False

                if isinstance(oToken, parser.open_parenthesis):
                    lColumn.append(iColumn + iPreviousColumn - iIndent)
                    print(f'Open Paren = {lColumn}')


    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.unique_id)
            self._filter_out_fix_only_violations(dFixOnly)
            for oViolation in self.violations[::-1]:
                self._fix_violation(oViolation)
            oFile.update(self.violations)
            self.clear_violations()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        print(dAction)
        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            lTokens.insert(0, parser.whitespace(' '*dAction['column']))

        oViolation.set_tokens(lTokens)


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
    print(f'Start Column = {iReturn}')
    return iReturn


def _find_first_column(oFile, oToi, bAlignLeft):
    if bAlignLeft:
        iFirstColumn = oFile.get_column_of_token_index(oToi.get_start_index())
        iNextColumn = 2
    else:
        iFirstColumn = oFile.get_column_of_token_index(oToi.get_start_index())
        iNextColumn = iFirstColumn
    return iFirstColumn, iNextColumn
