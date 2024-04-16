# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_300(token_indent):
    """
    This rule checks the indent of the block label.

    **Violation**

    .. code-block:: vhdl

       a <= b;

          block_label : block is

    **Fix**

    .. code-block:: vhdl

       a <= b;

       block_label : block is
    """

    def __init__(self):
        super().__init__(lTokens)
