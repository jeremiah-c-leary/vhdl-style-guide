
from vsg.rules.port import port_rule

import re


class rule_017(port_rule):
    '''
    Port rule 017 checks the "port" keyword is lowercase.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Change "port" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if not re.match('^\s*port', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'port')
