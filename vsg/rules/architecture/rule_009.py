
from vsg.rules.architecture import architecture_rule

import re


class rule_009(architecture_rule):
    '''Architecture rule 009 checks for the "end" and "architecture" keyword are lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Ensure "end" and "architecture" keywords are lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if re.match('^\s*end\s\s*architecture', oLine.lineLower):
                    if not re.match('^\s*end\s\s*architecture', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'end')
            self._lower_case(oFile.lines[iLineNumber], 'architecture')
