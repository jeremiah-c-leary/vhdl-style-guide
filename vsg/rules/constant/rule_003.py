
from vsg.rules.constant import constant_rule

import re


class rule_003(constant_rule):
    '''
    Constant rule 003 checks there is a single space after the "constant" keyword.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "constant" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'constant')
