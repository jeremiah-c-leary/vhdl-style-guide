
from vsg import rule
from vsg import fix


class rule_021(rule.rule):
    '''
    Process rule 021 checks for blank lines between the end of the sensitivity list and before the "begin" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '021')
        self.solution = 'Remove blank lines between the end of the sensitivity list and before the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                if oLine.isProcessBegin and oLine.isSensitivityListEnd:
                    fSkipProcess = True
                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
                    fSkipProcess = True
                if fSkipProcess:
                    if oLine.isEndProcess:
                        fSkipProcess = False
                    continue  # pragma: no cover
                if oLine.isProcessBegin:
                    if fBlanksFound and not fNonBlanksFound:
                        self.add_violation(iLineNumber)
                    fCheckForBlanks = False
                    fBlanksFound = False
                    fNonBlanksFound = False
                    fSkipProcess = True
                if fCheckForBlanks:
                    if oLine.isBlank:
                        fBlanksFound = True
                    else:
                        fNonBlanksFound = True
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.remove_blank_lines_above(self, oFile, iLineNumber)
