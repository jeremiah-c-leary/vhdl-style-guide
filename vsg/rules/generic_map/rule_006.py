
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.generic_map_aspect.map_keyword, token.generic_map_aspect.open_parenthesis])
lTokens.append([token.port_map_aspect.map_keyword, token.port_map_aspect.open_parenthesis])


class rule_006(Rule):
    '''
    This rule checks for a single space between the **map** keyword and the (.

    **Violation**

    .. code-block:: vhdl

       generic map(

       generic map   (

    **Fix**

    .. code-block:: vhdl

       generic map (

       generic map (
    '''
    def __init__(self):
        Rule.__init__(self, 'generic_map', '006', lTokens)
        self.solution = 'Ensure a single space exists between "map" and (.'
