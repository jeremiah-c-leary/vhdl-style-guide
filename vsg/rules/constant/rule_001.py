# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.constant_declaration.constant_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of a constant declaration.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is

       constant size : integer := 1;
           constant width : integer := 32

    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         constant size : integer := 1;
         constant width : integer := 32
    """

    def __init__(self):
        super().__init__(lTokens)
