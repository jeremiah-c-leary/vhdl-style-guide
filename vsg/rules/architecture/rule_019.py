
from vsg.rules.architecture import architecture_rule

import re


class rule_019(architecture_rule):
    '''Architecture rule 019 checks the "of" keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Change "of" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*\w+\s+\w+\s+of', oLine.lineLower):
                    if not re.match('^\s*\w+\s+\w+\s+of', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'of')
