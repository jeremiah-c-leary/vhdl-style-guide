
from vsg import rule

import re


class rule_024(rule.rule):
    '''
    Architecture rule 024 checks for the architecture name in the "end architecture" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '024')
        self.solution = 'Add architecture name keyword.'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture and not re.match('^\s*end\s+architecture\s+\w+', oLine.line, re.IGNORECASE):
                if re.match('^\s*end\s+architecture', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
                elif not re.match('^\s*end\s+\w+', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
