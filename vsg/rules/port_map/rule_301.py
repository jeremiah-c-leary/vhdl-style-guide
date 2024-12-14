# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent_between_tokens

lTokens = []
lTokens.append(token.association_element.formal_part)

oStart = token.port_map_aspect.port_keyword
oEnd = token.port_map_aspect.close_parenthesis


class rule_301(token_indent_between_tokens):
    """
    This rule checks for the proper indentation of association elements in port maps.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
               WR_EN    => wr_en,
       RD_EN    => rd_en,
             OVERFLOW => overflow
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
        super().__init__(lTokens, oStart, oEnd, bInclusive=True)
