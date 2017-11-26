
from vsg.rules.constant import constant_rule


class rule_004(constant_rule):
    '''
    Constant rule 004 checks the constant name is lowercase.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change constant name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
