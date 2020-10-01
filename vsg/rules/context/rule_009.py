
from vsg.rules import move_token_next_to_another_token

from vsg.token import context_declaration as token


class rule_009(move_token_next_to_another_token):
    '''
    Checks the context is keyword on the same line as the context identifier.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'context', '009', token.end_keyword, token.end_context_keyword)
        self.subphase = 1
        self.solution = 'Move identifier next to end keyword'
