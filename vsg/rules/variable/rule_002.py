
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    Signal rule 002 checks the "variable" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'variable', '002', 'isVariable', 'variable')
        self.solution = 'Lowercase "variable" keyword.'
