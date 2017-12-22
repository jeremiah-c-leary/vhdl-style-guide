
from vsg import rule

import re


class rule_008(rule.rule):
    '''
    Port rule 008 checks for three spaces after "out" keyword in a port declaration for "out" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '008')
        self.solution = 'Change the number of spaces after the "out" keyword to three spaces.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                if not re.match('^\s*\S+\s*:\s*out\s\s\s\S+', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:\s*out)(\s*)', r'\1   ', oLine.line, flags=re.IGNORECASE))
