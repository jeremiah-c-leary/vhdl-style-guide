
from vsg.rules import single_space_before_rule


class rule_010(single_space_before_rule):
    '''
    Constant rule 010 checks for a single space before the := keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self)
        self.name = 'constant'
        self.identifier = '010'
        self.solution = 'Add a space before the := assignment.'
        self.sTrigger = 'isConstant'
        self.sWord = ':='
