
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_009(rule.Rule):
    '''
    Checks the alignment of multiline concurrent conditional signal assignments.

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
        rule.Rule.__init__(self, 'concurrent', '009')
        self.solution = 'Align with open parenthesis on previous line.'
        self.phase = 5
        self.subphase = 2
        self.lTokenPairs = lTokenPairs

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.lTokenPairs[0][0], self.lTokenPairs[0][1])

        for oToi in lToi:

            iLine, lTokens = utils.get_toi_parameters(oToi)
#            print('> ' + str(iLine) + ' <' + '-'*80)

            iStartColumn = calculate_start_column(oFile, oToi)
            lColumn = []
            lColumn.append(iStartColumn)
            iFirstColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iColumn = iFirstColumn
            iIndent = 0
            bWaveform = True
            bCondition = False
            iWhenColumn = 0
            iPreviousColumn = 0
#            print('-'*80)
            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.carriage_return):
#                    print(f'--> Line Number | {iLine} <' + '-'*80)
                    iPreviousColumn = lColumn[-1]
                    iColumn = 0
                    iIndent = calculate_indent(iToken, lTokens)
                    oNextToken = lTokens[iToken + 1]
                    if bWaveform:
                        if isinstance(oNextToken, parser.whitespace):
                            if len(oNextToken.get_value()) != iStartColumn:
                                dAction = {}
                                dAction['line'] = iLine
                                dAction['column'] = iStartColumn
                                dAction['action'] = 'adjust'
                                dAction['previous'] = iPreviousColumn
                                sSolution = 'Adjust indent to column ' + str(iIndent + lColumn[-1])
                                oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                                oViolation.set_action(dAction)
                                self.add_violation(oViolation)
                        else:
                            dAction = {}
                            dAction['line'] = iLine
                            dAction['column'] = iStartColumn
                            dAction['action'] = 'insert'
                            dAction['previous'] = iPreviousColumn
                            sSolution = 'Adjust indent to column ' + str(iStartColumn)
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                    if bCondition:
                        if isinstance(oNextToken, parser.whitespace):
                            oSecondToken = lTokens[iToken + 2]
                            if isinstance(oSecondToken, parser.close_parenthesis):
                                iAdjustIndex = -2
                            else:
                                iAdjustIndex = -1
                            if len(oNextToken.get_value()) != lColumn[iAdjustIndex]:
                                dAction = {}
                                dAction['line'] = iLine
                                dAction['column'] = lColumn[-1]
                                dAction['action'] = 'adjust'
                                dAction['previous'] = iPreviousColumn
                                sSolution = 'Adjust indent to column ' + str(iIndent + lColumn[iAdjustIndex])
                                oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                                oViolation.set_action(dAction)
                                self.add_violation(oViolation)
                        else:
                            if isinstance(oNextToken, parser.close_parenthesis):
                                iAdjustIndex = -2
                            else:
                                iAdjustIndex = -1
                            dAction = {}
                            dAction['line'] = iLine
                            dAction['column'] = lColumn[iAdjustIndex]
                            dAction['action'] = 'insert'
                            dAction['previous'] = iPreviousColumn
                            sSolution = 'Adjust indent to column ' + str(lColumn[iAdjustIndex])
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)

#                    print(f'{iLine} | {iIndent} | {bWaveform} | {bCondition} | {lColumn} | {iPreviousColumn}')
                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, token.conditional_waveforms.when_keyword):
                    bWaveform = False
                    bCondition = True
                    iWhenColumn = iColumn + 1
                    lColumn.append(iWhenColumn)
                if isinstance(oToken, token.conditional_waveforms.else_keyword):
                    bWaveform = True
                    bCondition = False
#                    lColumn.pop()

                if isinstance(oToken, parser.open_parenthesis):
#                    print(f'== {iColumn} + {iPreviousColumn} - {iIndent} = {iColumn + iPreviousColumn - iIndent}')
                    lColumn.append(iColumn + iPreviousColumn - iIndent)
#                    lColumn.append(iPreviousColumn - iColumn + iIndent)

                if isinstance(oToken, parser.close_parenthesis):
                    lColumn.pop()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(dAction)
        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            lTokens.insert(0, parser.whitespace(' '*dAction['column']))

        oViolation.set_tokens(lTokens)


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
    return iReturn


def calculate_indent(iToken, lTokens):
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iIndent = len(lTokens[iToken + 1].get_value())
    else:
        iIndent = 0
    return iIndent
