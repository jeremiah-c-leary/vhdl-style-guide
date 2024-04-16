# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent_between_tokens

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)
lTokens.append(token.component_instantiation_statement.semicolon)

lTokens.append(token.generic_map_aspect.generic_keyword)
lTokens.append(token.generic_map_aspect.close_parenthesis)

lTokens.append(token.port_map_aspect.port_keyword)
lTokens.append(token.port_map_aspect.close_parenthesis)

lTokens.append(token.association_element.formal_part)

oStart = token.component_instantiation_statement.instantiation_label
oEnd = token.component_instantiation_statement.semicolon


class rule_001(token_indent_between_tokens):
    """
    This rule checks for the proper indentation of instantiations.

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
