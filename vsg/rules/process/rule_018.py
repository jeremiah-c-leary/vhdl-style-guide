
from vsg.rules.process import process_rule

import re


class rule_018(process_rule):
    '''
    Process rule 018 checks the "end process" has a label.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add a label for the "end process".'
        self.phase = 1
        self.fixable = False  # The user must add the label

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                      self.add_violation(iLineNumber)
