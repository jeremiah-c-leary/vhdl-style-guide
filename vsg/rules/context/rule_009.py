
from vsg.rules import move_token_next_to_another_token_if_it_exists_between_tokens

from vsg.token import context_declaration as token

lBetweenTokens = [token.end_keyword, token.semicolon]


class rule_009(move_token_next_to_another_token_if_it_exists_between_tokens):
    '''
    Checks the context is keyword on the same line as the context identifier.
    '''

    def __init__(self):
        move_token_next_to_another_token_if_it_exists_between_tokens.__init__(self, 'context', '009', token.end_keyword, token.end_context_keyword, lBetweenTokens)
        self.subphase = 1
        self.solution = 'Move identifier next to *end* keyword'
