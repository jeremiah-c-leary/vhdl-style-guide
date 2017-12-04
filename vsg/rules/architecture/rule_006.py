
from vsg.rules.architecture import architecture_rule

import re


class rule_006(architecture_rule):
    '''Architecture rule 006 checks if the "is" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure "is" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1
        self.fixable = False  # There is an example of this for entity

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and not re.match('^\s*architecture\s+\w+\s+of\s+\w+\s+is', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)
