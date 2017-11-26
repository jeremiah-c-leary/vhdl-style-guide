
from vsg.rules.constant import constant_rule

import re


class rule_006(constant_rule):
    '''
    Constant rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if re.match('^\s*constant\s+\S+:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
