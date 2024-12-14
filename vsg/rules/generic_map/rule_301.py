# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent_between_tokens

lTokens = []
lTokens.append(token.association_element.formal_part)

oStart = token.generic_map_aspect.generic_keyword
oEnd = token.generic_map_aspect.close_parenthesis


class rule_301(token_indent_between_tokens):
    """
    This rule checks for the proper indentation of association elements in generic maps.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
               G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
             G_GEN3 => g_gen3
         );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
           G_GEN1 => g_gen1,
           G_GEN2 => g_gen2,
           G_GEN3 => g_gen3
         );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, bInclusive=True)
