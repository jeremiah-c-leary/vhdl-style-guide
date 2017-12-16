
from vsg.rules import single_space_after_rule


class rule_002(single_space_after_rule):
    '''
    Function rule 002 checks there is a single space between the function keyword and the function name.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'function', '002', 'isFunctionKeyword', 'function')
        self.solution = 'Ensure a single space exists between the "function" keyword and the function name.'
