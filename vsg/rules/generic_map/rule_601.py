
from vsg.rules import token_prefix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.association_element.formal_part)

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis

class rule_601(token_prefix_between_tokens):
    '''
    Checks for prefixes in generic map names.
    '''

    def __init__(self):
        token_prefix_between_tokens.__init__(self, 'generic_map', '601', lTokens, lStart, lEnd)
        self.prefixes = ['g_']
