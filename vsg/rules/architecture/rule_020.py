
from vsg.rules.architecture import architecture_rule

import re


class rule_020(architecture_rule):
    '''Architecture rule 020 checks the "is" keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '020'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*architecture\s+\w+\s+of\s+\w+\s+is', oLine.lineLower):
                    if not re.match('^\s*\w+\s+\w+\s+\w+\s+\w+\s+is', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'is')
