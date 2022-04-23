
from vsg.rules import token_suffix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.association_element.formal_part)

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis

class rule_600(token_suffix_between_tokens):
    '''
    Checks for suffixes in generic map names.
    '''

    def __init__(self):
        token_suffix_between_tokens.__init__(self, 'generic_map', '600', lTokens, lStart, lEnd)
        self.suffixes = ['_g']
