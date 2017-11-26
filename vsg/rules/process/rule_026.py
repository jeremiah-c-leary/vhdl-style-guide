
from vsg.rules.process import process_rule


class rule_026(process_rule):
    '''
    Process rule 026 checks for blank lines between the end of the sensitivity list and process declarative lines.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '026'
        self.solution = 'Ensure a single blank line between the end of the sensitivity list and the next non-blank line.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        iBlankCount = 0
        iFailingLineNumber = 0
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
                    else:
                        if not iBlankCount == 1 and not oLine.isProcessBegin:
                            self.add_violation(iFailingLineNumber)
                        fSkipProcess = True
                        fCheckForBlanks = False
                        iBlankCount = 0
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True
                    iFailingLineNumber = iLineNumber

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
            oFile.lines[iLineNumber + 1].insideProcess = True
