
from vsg.rules import single_space_after_rule


class rule_005(single_space_after_rule):
    '''
    If rule 005 checks there is a single space between the "elsif" keyword and the (.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'if', '005', 'isElseIfKeyword', 'elsif')
        self.solution = 'Ensure only a single space exists between the "elsif" keyword and the (.'
