
from vsg.rules.constant import constant_rule

import re


class rule_002(constant_rule):
    '''
    Constant rule 002 checks the "constant" keyword is lowercase.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lower case "constant" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'constant')
