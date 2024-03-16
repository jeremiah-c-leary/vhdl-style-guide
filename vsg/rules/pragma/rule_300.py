# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.pragma.open)
lTokens.append(token.pragma.close)
lTokens.append(token.pragma.single)


class rule_300(Rule):
    """
    This rule checks the indent of pragmas.

    |configuring_pragmas_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

       -- synthesis translate_off
         signal wr_en : std_logic;
         signal rd_en : std_Logic;
       -- synthesis translate_on

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         -- synthesis translate_off
         signal wr_en : std_logic;
         signal rd_en : std_Logic;
         -- synthesis translate_on

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
