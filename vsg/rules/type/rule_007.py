
from vsg.rules.type import type_rule

import re


class rule_007(type_rule):
    '''
    Type rule 007 checks for a single space after the "is" keyword.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure a single space after the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^.*\sis\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'is')
