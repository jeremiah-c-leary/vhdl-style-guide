
from vsg import rule
from vsg import utils

import re


class rule_020(rule.rule):
    '''
    Port rule 020 checks there is at least one space before the :.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '020')
        self.solution = 'Add a space before the :.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration and not re.match('^.*\s+:', oLine.line):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            oLine.update_line(oLine.line.replace(':', ' :'))
