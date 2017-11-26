
from vsg.rules.constant import constant_rule

import re


class rule_005(constant_rule):
    '''
    Constant rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a single space after the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant\s+\w+\s*:\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
