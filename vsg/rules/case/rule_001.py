
from vsg import rule
from vsg import check
from vsg import fix


class rule_001(rule.rule):
    '''Case rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        rule.rule.__init__(self, 'case', '001')
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseKeyword or oLine.isCaseWhenKeyword or oLine.isEndCaseKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
