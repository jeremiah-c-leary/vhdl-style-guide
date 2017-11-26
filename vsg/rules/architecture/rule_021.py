
from vsg.rules.architecture import architecture_rule

import re


class rule_021(architecture_rule):
    '''Architecture rule 021 checks the "begin" keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '021'
        self.solution = 'Change "begin" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureBegin:
                if not re.match('^\s*begin', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'begin')
