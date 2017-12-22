
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    If rule 003 checks there is a single space between the if keyword and the (.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'if', '003', 'isIfKeyword', 'if')
        self.solution = 'Ensure only a single space exists between the "if" keyword and the (.'
