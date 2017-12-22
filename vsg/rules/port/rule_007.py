
from vsg import rule

import re


class rule_007(rule.rule):
    '''
    Port rule 007 checks for four spaces after the "in" keyword in a port declaration for "in" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '007')
        self.solution = 'Change the number of spaces after the "in" keyword to four spaces.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and re.match('^\s*\S+\s*:\s*in\s', oLine.lineLower):
                if not re.match('^\s*\S+\s*:\s*in\s\s\s\s\S+', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:\s*in)(\s*)', r'\1    ', oLine.line, flags=re.IGNORECASE))
