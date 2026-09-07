# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.blank_line_above_line_starting_with_token_when_between_tokens import Rule

lTokens = []
lTokens.append(token.association_element.formal_part)


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
        super().__init__(lTokens)
        self.style = "no_blank_line"
        self.lBetweenTokenPairs = [token.generic_map_aspect.open_parenthesis, token.generic_map_aspect.close_parenthesis]
