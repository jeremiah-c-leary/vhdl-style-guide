
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token
from vsg.token import iteration_scheme


class rule_005(single_space_between_tokens):
    '''
    Checks for a single space between the label and :.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'for_loop', '005', token.label_colon, iteration_scheme.for_keyword)
        self.solution = 'Ensure a single space between label and :.'
