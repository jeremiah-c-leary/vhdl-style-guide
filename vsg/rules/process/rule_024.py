
from vsg.rules.process import process_rule

import re


class rule_024(process_rule):
    '''
    Process rule 024 checks for a single space after the process label and the :.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '024'
        self.solution = 'Ensure a single space exists between process label and :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:', oLine.line):
                    if not re.match('^\s*\S+\s:', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
