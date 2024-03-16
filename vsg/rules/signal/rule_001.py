# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.signal_declaration.signal_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of signal declarations.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

       signal wr_en : std_logic;
            signal rd_en : std_logic;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         signal wr_en : std_logic;
         signal rd_en : std_logic;

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
