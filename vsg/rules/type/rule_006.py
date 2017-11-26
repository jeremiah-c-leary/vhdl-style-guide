
from vsg.rules.type import type_rule

import re


class rule_006(type_rule):
    '''
    Type rule 006 checks for a single space before the "is" keyword.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure a single space before the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^\s*type\s*\w+\sis', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], 'is')
