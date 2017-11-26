
from vsg.rules.process import process_rule

import re


class rule_016(process_rule):
    '''
    Process rule 016 checks a process has a label.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Add a label for the process.'
        self.phase = 1
        self.fixable = False   # The user must add the label

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not re.match('^\s*\S+\s*:', oLine.line):
                      self.add_violation(iLineNumber)
