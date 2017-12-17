
from vsg import rule

import re


class rule_018(rule.rule):
    '''
    Process rule 018 checks the "end process" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '018')
        self.solution = 'Add a label for the "end process".'
        self.phase = 1
        self.fixable = False  # The user must add the label

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess and not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                self.add_violation(iLineNumber)
