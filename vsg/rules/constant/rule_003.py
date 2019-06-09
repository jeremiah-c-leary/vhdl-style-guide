
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Constant rule 003 checks the number of spaces after the "constant" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'constant', '003', 'isConstant', 'constant')
