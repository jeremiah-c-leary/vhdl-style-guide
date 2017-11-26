
from vsg.rules.variable import variable_rule

import re


class rule_006(variable_rule):
    '''
    Signal rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+.*\S:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
