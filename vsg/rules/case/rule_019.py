
from vsg import rule
from vsg import utils

import re


class rule_019(rule.rule):
    '''
    Case rule 019 checks for labels before the case case keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '019')
        self.phase = 1
        self.solution = 'Remove label before "case" keyword'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.hasCaseLabel:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub('^(\s*)(\w+\s*:\s*)', r'\1', oLine.line, 1))
            oLine.hasCaseLabel = False
