
from vsg.rules.architecture import architecture_rule

import re


class rule_024(architecture_rule):
    '''
    Architecture rule 024 checks for the architecture name in the "end architecture" statement.
    '''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '024'
        self.solution = 'Add architecture name keyword.'
        self.phase = 1
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                if not re.match('^\s*end\s+architecture\s+\w+', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
