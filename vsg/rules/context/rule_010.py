
from vsg.rules import move_token_next_to_another_token

from vsg.token import context_declaration as token


class rule_010(move_token_next_to_another_token):
    '''
    Checks the context is keyword on the same line as the context identifier.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'context', '010', token.end_context_keyword, token.context_simple_name)
        self.subphase = 2
        self.solution = 'Move context_simple_name next to context keyword'
