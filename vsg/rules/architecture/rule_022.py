
from vsg.rules.architecture import architecture_rule

import re


class rule_022(architecture_rule):
    '''
    Architecture rule 022 checks for a single space after the "end architecture" keywords and the architecture name.
    '''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '022'
        self.solution = 'Ensure a single space exists between "architecture" and the architecture name.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if re.match('^\s*end\s+architecture\s+\w', oLine.lineLower):
                    if not re.match('^\s*end\s+architecture\s\w', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'architecture')
