
from vsg import token

from vsg.rules import single_space_between_token_pairs_bounded_by_tokens

lTokens = []
lTokens.append([token.association_element.assignment, token.association_element.actual_part])

lStart = token.port_map_aspect.open_parenthesis
lEnd = token.port_map_aspect.close_parenthesis


class rule_007(single_space_between_token_pairs_bounded_by_tokens):
    '''
    Checks for a single space after the => operator in port maps.
    '''
    def __init__(self):
        single_space_between_token_pairs_bounded_by_tokens.__init__(self, 'port_map', '007', lTokens, lStart, lEnd)
        self.solution = 'Only a single space after => operator.'
