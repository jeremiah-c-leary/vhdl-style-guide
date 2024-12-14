# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.generic_map_aspect.close_parenthesis)


class rule_302(token_indent):
    """
    This rule checks for the proper indentation of the closing parenthesis in generic maps.

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
        super().__init__(lTokens)
