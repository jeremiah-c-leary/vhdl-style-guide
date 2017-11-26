
from vsg.rules.if_statement import if_rule

import re


class rule_003(if_rule):
    '''If rule 003 checks there is a single space between the if keyword and the (.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure only a single space exists between the "if" keyword and the (.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isIfKeyword:
                if re.match('^\s*if\s*\(', oLine.lineLower):
                    if not re.match('^\s*if\s\(', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'if')
