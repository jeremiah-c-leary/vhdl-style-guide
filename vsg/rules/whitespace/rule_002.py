
from vsg import rule
from vsg import utils


class rule_002(rule.rule):
    '''Whitespace rule 002 checks for tabs in lines'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '002')
        self.phase = 2
        self.solution = 'Replace tabs with spaces.'
        self.phase = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if '\t' in oLine.line:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(oLine.line.replace('\t', '  '))
