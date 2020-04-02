
from vsg import rule
from vsg import utils

import re


class rule_007(rule.rule):
    '''
    Port rule 007 checks for four spaces after the "in" keyword in a port declaration for "in" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '007')
        self.solution = 'Change the number of spaces after the "in" keyword to four spaces.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration and re.match('^\s*\S+\s*:\s*in\s', oLine.lineLower):
            if not re.match('^\s*\S+\s*:\s*in\s\s\s\s\S+', oLine.lineLower):
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            oLine.update_line(re.sub(r'^(\s*\S+\s*:\s*in)(\s*)', r'\1    ', oLine.line, flags=re.IGNORECASE))
