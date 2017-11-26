
from vsg.rules.port import port_rule

import re


class rule_005(port_rule):
    '''
    Port rule 005 checks for a single space after the colon in a port declaration for "in" and "inout" ports.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*in', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sin', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:)(\s*)', r'\1 ', oLine.line, flags=re.IGNORECASE))
