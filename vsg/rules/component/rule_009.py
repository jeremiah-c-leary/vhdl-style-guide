# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_009(token_indent):
    """
    This rule checks the indent of the **end component** keywords.

    **Violation**

    .. code-block:: vhdl

          overflow : std_logic
        );
            end component fifo;

    **Fix**

    .. code-block:: vhdl

           overflow : std_logic
         );
       end component fifo;
    """

    def __init__(self):
        super().__init__(lTokens)
