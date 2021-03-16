
from vsg.rules import move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens

from vsg.token import context_declaration as token

lAnchorTokens = []
lAnchorTokens.append(token.end_keyword)
lAnchorTokens.append(token.end_context_keyword)

oToken = token.context_simple_name

oStartToken = token.end_keyword
oEndToken = token.semicolon


class rule_010(move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens):
    '''
    Checks the context_context_simple_name is next to the context keyword.
    '''

    def __init__(self):
        move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens.__init__(self, 'context', '010', oToken, lAnchorTokens, oStartToken, oEndToken, bInsertWhitespace=True)
        self.subphase = 2
        self.solution = 'Move context_simple_name next to *context* keyword'
