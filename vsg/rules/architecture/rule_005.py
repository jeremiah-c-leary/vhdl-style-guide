
from vsg import rule

import re


class rule_005(rule.rule):
    '''Architecture rule 005 checks if the "of" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'
        self.identifier = '005'
        self.solution = 'Ensure "of" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1
        self.fixable = False  # There is an example of this for entity

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and not re.match('^\s*architecture\s+\w+\s+of', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)
