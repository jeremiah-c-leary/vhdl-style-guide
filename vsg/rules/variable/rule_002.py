
from vsg.rules.variable import variable_rule


class rule_002(variable_rule):
    '''
    Signal rule 002 checks the "variable" keyword is lowercase.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "variable" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'variable')
