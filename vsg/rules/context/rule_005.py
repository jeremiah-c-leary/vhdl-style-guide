
from vsg.rules import move_token_next_to_another_token

from vsg.token import context_declaration as token


class rule_005(move_token_next_to_another_token):
    '''
    Checks the "context" identifier is on the same line as the "context" keyword.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'context', '005', token.context_keyword, token.identifier)
        self.subphase = 1
        self.solution = 'Move identifier next to *context* keyword'
