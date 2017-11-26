
from vsg.rules.port import port_rule

import re


class rule_003(port_rule):
    '''
    Port rule 003 checks spacing between "port" and the open parenthesis.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Change spacing between "port" and "(" to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(port)\s*\(', r'\1 (', oLine.line, flags=re.IGNORECASE))
