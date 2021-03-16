
from vsg.rules import move_token_next_to_another_token

from vsg.token import generic_clause as token


class rule_018(move_token_next_to_another_token):
    '''
    Checks the **generic** keyword is on the same line as the (.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'generic', '018', token.generic_keyword, token.open_parenthesis)
        self.solution = 'Move the ( to the same line as the *generic* keyword.'
