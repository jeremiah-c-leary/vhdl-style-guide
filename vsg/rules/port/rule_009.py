
from vsg.rules.port import port_rule

import re


class rule_009(port_rule):
    '''
    Port rule 009 checks for a single space after "inout" keyword in a port declaration for "inout" ports.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Change the number of spaces after the "inout" keyword to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^\s*\S+\s*:\s*inout', oLine.lineLower):
                    if not re.match('^\s*\S+\s*:\s*inout\s\S+', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*\S+\s*:\s*inout)(\s*)', r'\1 ', oLine.line, flags=re.IGNORECASE))
