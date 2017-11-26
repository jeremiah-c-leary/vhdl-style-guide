
from vsg.rules.architecture import architecture_rule

import re


class rule_012(architecture_rule):
    '''Architecture rule 012 checks for a single space between the "end" and "architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Single space between "end" and "architecture" keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if (len(oLine.line.split()) > 1):
                    if re.match('^\s*end\s+architecture', oLine.lineLower):
                        if not re.match('^\s*end\sarchitecture', oLine.lineLower):
                            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'end')
