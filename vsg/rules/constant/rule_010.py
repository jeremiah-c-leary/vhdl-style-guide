
from vsg.rules import single_space_before_character_rule


class rule_010(single_space_before_character_rule):
    '''
    Constant rule 010 checks for at least a single space before the := keyword.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self)
        self.name = 'constant'
        self.identifier = '010'
        self.solution = 'Add a space before the := assignment.'
        self.sTrigger = 'isConstant'
        self.sWord = ':='
