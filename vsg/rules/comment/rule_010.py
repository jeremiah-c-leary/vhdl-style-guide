# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules import token_indent_unless_between_tokens
from vsg.token import constant_declaration

lTokens = []
lTokens.append(parser.comment)

lUnless = []
lUnless.append([constant_declaration.constant_keyword, constant_declaration.semicolon])


class rule_010(token_indent_unless_between_tokens):
    """
    This rule checks the indent lines starting with comments.

    **Violation**

    .. code-block:: vhdl

           -- Libraries
       library ieee;

        -- Define architecture
       architecture rtl of fifo is

       -- Define signals
         signal wr_en : std_logic;
         signal rd_en : std_Logic;

       begin

    **Fix**

    .. code-block:: vhdl

       -- Libraries
       library ieee;

       -- Define architecture
       architecture rtl of fifo is

         -- Define signals
         signal wr_en : std_logic;
         signal rd_en : std_Logic;

       begin
    """

    def __init__(self):
        super().__init__(lTokens, lUnless)
        self.phase = 4
        self.subphase = 3
