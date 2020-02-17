
from vsg import rule
from vsg import utils

import re


class rule_008(rule.rule):
    '''
    Port rule 008 checks for three spaces after "out" keyword in a port declaration for "out" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '008')
        self.solution = 'Change the number of spaces after the "out" keyword to three spaces.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration and re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
            if not re.match('^\s*\S+\s*:\s*out\s\s\s\S+', oLine.lineLower):
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:\s*out)(\s*)', r'\1   ', oLine.line, flags=re.IGNORECASE))
