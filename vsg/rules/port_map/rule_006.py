# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.port_map_aspect.map_keyword, token.port_map_aspect.open_parenthesis])


class rule_006(Rule):
    """
    This rule checks for a single space between the **map** keyword and the (.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       port map(

       port map   (

    **Fix**

    .. code-block:: vhdl

       port map (

       port map (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = 'Ensure a single space exists between "map" and (.'
