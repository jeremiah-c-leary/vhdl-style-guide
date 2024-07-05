# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_tokens_in_between_tokens import Rule

lTokens = []
lTokens.append(token.association_element.assignment)

oStart = token.port_map_aspect.open_parenthesis
oEnd = token.port_map_aspect.close_parenthesis


class rule_100(Rule):
    """
    This rule checks for at least a single space before the **=>** operator in port maps.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW=> overflow
         );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.number_of_spaces = ">=1"
