# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_009(token_indent):
    """
    This rule checks the indent of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

         wr_en : in    std_logic;
         rd_en : in    std_logic
       );
         end entity fifo;

    **Fix**

    .. code-block:: vhdl

           wr_en : in    std_logic;
           rd_en : in    std_logic
         );
       end entity fifo;
    """

    def __init__(self):
        super().__init__(lTokens)
