# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_302(token_indent):
    """
    This rule checks the indent of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       block_label : block is

       begin

         end block block_label;

    **Fix**

    .. code-block:: vhdl

       block_label : block is

       begin

       end block block_label;
    """

    def __init__(self):
        super().__init__(lTokens)
