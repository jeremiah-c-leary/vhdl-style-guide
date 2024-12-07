# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.generic_map_aspect.generic_keyword, token.generic_map_aspect.map_keyword])


class rule_101(Rule):
    """
    This rule checks for a single space between the **generic** keyword and the **map** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic       map(

    **Fix**

    .. code-block:: vhdl

       generic map (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = 'Ensure a single space exists between "generic" and "map".'
