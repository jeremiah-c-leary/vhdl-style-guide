# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_301(token_indent):
    """
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       block_label : block is

         begin

    **Fix**

    .. code-block:: vhdl

       block_label : block is

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
