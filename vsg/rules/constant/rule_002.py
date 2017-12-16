
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    Constant rule 002 checks the "constant" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'constant', '002', 'isConstant', 'constant')
