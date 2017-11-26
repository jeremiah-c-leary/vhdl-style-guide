
from vsg.rules.port import port_rule

import re


class rule_006(port_rule):
    '''
    Port rule 006 checks for one space after the colon in a port declaration for "out" ports.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change number of spaces before "out" to 3.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\sout', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:)(\s*)', r'\1 ', oLine.line, flags=re.IGNORECASE))
