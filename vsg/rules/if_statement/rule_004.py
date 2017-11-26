
from vsg.rules.if_statement import if_rule

import re


class rule_004(if_rule):
    '''If rule 004 checks there is a single space between the ) and "then" keyword.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure only a single space exists between the ) and "then" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword:
                if re.match('^\s*.*\)\s*then', oLine.lineLower):
                    if not re.match('^\s*.*\)\sthen', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], 'then')
