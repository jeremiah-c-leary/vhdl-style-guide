
from vsg import rule
from vsg import utils

import re


class rule_001(rule.rule):
    '''Whitespace rule 001 checks spaces at the end of lines.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '001')
        self.phase = 2
        self.solution = 'Remove trailing whitespace.'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.line.endswith(' '):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            oLine.update_line(re.sub(r'\s+$', '', oLine.line))
