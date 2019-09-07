
from vsg.rules import multiple_spaces_after_rule


class rule_003(multiple_spaces_after_rule):
    '''
    Constant rule 003 checks the number of spaces after the "constant" keyword.
    '''

    def __init__(self):
        multiple_spaces_after_rule.__init__(self, 'constant', '003', 'isConstant', 'constant')
