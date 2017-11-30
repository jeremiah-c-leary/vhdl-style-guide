
from vsg.rules.variable import variable_rule
from vsg import utilities
from vsg import fix
from vsg import check


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
                check.is_lowercase(self, utilities.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'variable')
