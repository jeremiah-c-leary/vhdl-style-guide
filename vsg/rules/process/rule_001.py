
from vsg.rules.process import process_rule
from vsg import check


class rule_001(process_rule):
    '''
    Process rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
