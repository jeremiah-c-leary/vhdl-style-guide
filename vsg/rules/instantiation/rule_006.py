
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.port_map_aspect.port_keyword)
lTokens.append(token.port_map_aspect.map_keyword)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_006(token_case_in_range_bounded_by_tokens):
    '''
    Checks the "port map" keywords have proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'instantiation', '006', lTokens, oStart, oEnd)
