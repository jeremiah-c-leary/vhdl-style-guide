
from vsg import rule


class rule_002(rule.rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '002')
        self.phase = 2
        self.solution = 'Replace tabs with spaces.'
        self.phase = 0

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if '\t' in oLine.line:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.replace('\t', '  '))
