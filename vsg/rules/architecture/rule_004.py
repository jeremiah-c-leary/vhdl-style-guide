
from vsg.rules.architecture import architecture_rule

import re


class rule_004(architecture_rule):
    '''Architecture rule 004 checks the architecture keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change architecture keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if not re.match('^\s*architecture', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'architecture')
