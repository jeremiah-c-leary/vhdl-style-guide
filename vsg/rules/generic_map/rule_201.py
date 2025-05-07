# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_lines_between_token_pairs as Rule

lTokenPairs = []
lTokenPairs.append([token.generic_map_aspect.open_parenthesis, token.generic_map_aspect.close_parenthesis])

class rule_201(Rule):
    """
    This rule checks for blank lines in a generic map.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

      generic map (
        G_GEN_1 => 3,
        G_GEN_2 => 4,

        G_GEN_3 => 5
      )
      port map (
        PORT_1 => w_port_1,
        PORT_2 => w_port_2,
        PORT_3 => w_port_3
      );

    **Fix**

    .. code-block:: vhdl

      generic map (
        G_GEN_1 => 3,
        G_GEN_2 => 4,
        G_GEN_3 => 5
      )
      port map (
        PORT_1 => w_port_1,
        PORT_2 => w_port_2,
        PORT_3 => w_port_3
      );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
