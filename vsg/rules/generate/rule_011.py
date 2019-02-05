
from vsg import rule

import re


class rule_011(rule.rule):
    '''
    Generate rule 011 checks the "end generate" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '011')
        self.solution = 'Add a label for the "end generate".'
        self.phase = 1
        self.fixable = False  # The user must add the label

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd and not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                self.add_violation(iLineNumber)
