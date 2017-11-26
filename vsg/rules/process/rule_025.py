
from vsg.rules.process import process_rule

import re


class rule_025(process_rule):
    '''
    Process rule 025 checks for a single space after the : and before the "process" keyword.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '025'
        self.solution = 'Ensure a single space exists between the : and the "process" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:\s*\S+', oLine.line):
                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
