
from vsg.rules import single_space_before_rule


class rule_004(single_space_before_rule):
    '''
    If rule 004 checks there is a single space between the ) and "then" keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self, 'if', '004', 'isThenKeyword', 'then')
        self.solution = 'Ensure only a single space exists between the ) and "then" keyword.'
