
from vsg.rules import move_token_to_the_right_of_several_possible_tokens

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)
lTokens.append(token.context_declaration.end_context_keyword)
lTokens.append(token.context_declaration.context_simple_name)

oToken = token.context_declaration.semicolon


class rule_011(move_token_to_the_right_of_several_possible_tokens):
    '''
    Checks the context semicolon is on the same line as the end context keyword.
    '''

    def __init__(self):
        move_token_to_the_right_of_several_possible_tokens.__init__(self, 'context', '011', oToken, lTokens)
