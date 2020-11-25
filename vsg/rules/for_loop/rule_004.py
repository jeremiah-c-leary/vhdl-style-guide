
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token


class rule_004(single_space_between_tokens):
    '''
    Checks for a single space between the label and :.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'for_loop', '004', token.loop_label, token.label_colon)
        self.solution = 'Ensure a single space between label and :.'
