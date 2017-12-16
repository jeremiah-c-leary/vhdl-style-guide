
from vsg.rules import lower_case_rule


class rule_004(lower_case_rule):
    '''
    Function rule 004 checks the "begin" keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'function', '004', 'isFunctionBegin', 'begin')
        self.solution = 'Lowercase the "begin" keyword.'
