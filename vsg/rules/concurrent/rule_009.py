
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
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'concurrent', '009')
        self.phase = 5
        self.subphase = 2
        self.lTokenPairs = lTokenPairs

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.lTokenPairs[0][0], self.lTokenPairs[0][1])

        for oToi in lToi:

            iLine, lTokens = utils.get_toi_parameters(oToi)

            iStartColumn = calculate_start_column(oFile, oToi)
            lColumn = []
            lColumn.append(iStartColumn)
            iColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iIndent = 0
            bWaveform = True
            bCondition = False
            iPreviousColumn = 0

            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.carriage_return):
                    iPreviousColumn = lColumn[-1]
                    iColumn = 0
                    iIndent = calculate_indent(iToken, lTokens)
                    oNextToken = lTokens[iToken + 1]
                    if bWaveform:
                        iAdjustIndex = -1
                        if isinstance(oNextToken, parser.whitespace):
                            if len(oNextToken.get_value()) != iStartColumn:
                                oViolation = build_violation(iLine, iStartColumn, 'adjust', oToi, iToken)
                                self.add_violation(oViolation)
                        else:
                            oViolation = build_violation(iLine, iStartColumn, 'insert', oToi, iToken)
                            self.add_violation(oViolation)
                    if bCondition:
                        if isinstance(oNextToken, parser.whitespace):
                            oSecondToken = lTokens[iToken + 2]
                            if isinstance(oSecondToken, parser.close_parenthesis):
                                iAdjustIndex = -2
                            else:
                                iAdjustIndex = -1
                            if len(oNextToken.get_value()) != lColumn[iAdjustIndex]:
                                oViolation = build_violation(iLine, lColumn[iAdjustIndex], 'adjust', oToi, iToken)
                                self.add_violation(oViolation)
                        else:
                            if isinstance(oNextToken, parser.close_parenthesis):
                                iAdjustIndex = -2
                            else:
                                iAdjustIndex = -1
                            oViolation = build_violation(iLine, lColumn[iAdjustIndex], 'insert', oToi, iToken)
                            self.add_violation(oViolation)

                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, token.conditional_waveforms.when_keyword):
                    bWaveform = False
                    bCondition = True
                    lColumn.append(iColumn + 1)

                if isinstance(oToken, token.conditional_waveforms.else_keyword):
                    bWaveform = True
                    bCondition = False

                if isinstance(oToken, parser.open_parenthesis):
                    lColumn.append(iColumn + iPreviousColumn - iIndent)

                if isinstance(oToken, parser.close_parenthesis):
                    lColumn.pop()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
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


def build_violation(iLine, iColumn, sAction, oToi, iToken):
    dAction = {}
    dAction['line'] = iLine
    dAction['column'] = iColumn
    dAction['action'] = sAction
    sSolution = 'Adjust indent to column ' + str(iColumn)
    oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
    oViolation.set_action(dAction)
    return oViolation
