
from vsg.rules.process import process_rule


class rule_027(process_rule):
    '''
    Process rule 027 checks for blank lines between the process declarative lines and the "begin" keyword.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '027'
        self.solution = 'Ensure a single blank line between the last non-blank line and the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        iBlankCount = 0
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                if oLine.isProcessBegin and oLine.isSensitivityListEnd:
                    fSkipProcess = True
                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
                    fSkipProcess = True
                if fSkipProcess:
                    if oLine.isEndProcess:
                        fSkipProcess = False
                    continue  #  pragma: no cover
                if fCheckForBlanks:
                    if oLine.isBlank:
                        iBlankCount += 1
                    if not oLine.isBlank and not oLine.isProcessBegin:
                        iBlankCount = 0
                    if oLine.isProcessBegin:
                        if not iBlankCount == 1:
                            self.add_violation(iLineNumber)
                        fSkipProcess = True
                        fCheckForBlanks = False
                        iBlankCount = 0
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
            oFile.lines[iLineNumber].insideProcess = True
