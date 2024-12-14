# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent_between_tokens

lTokens = []
lTokens.append(token.generic_map_aspect.generic_keyword)
lTokens.append(token.generic_map_aspect.close_parenthesis)

lTokens.append(token.association_element.formal_part)

oStart = token.generic_map_aspect.generic_keyword
oEnd = token.generic_map_aspect.close_parenthesis


class rule_300(token_indent_between_tokens):
    """
    This rule checks for the proper indentation of instantiations.

    **Violation**

    .. code-block:: vhdl

         U_FIFO : FIFO
      generic map (
               WR_EN    => wr_en,
       RD_EN    => rd_en,
             OVERFLOW => overflow
                    );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, bInclusive=True)
