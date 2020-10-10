
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.generic_map_aspect.map_keyword, token.generic_map_aspect.open_parenthesis])


class rule_018(single_space_between_token_pairs):
    '''
   Checks for a single space before the (
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'instantiation', '018', lTokens)
        self.solution = 'Ensure a single space exists between "map" and (.'
