# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.entity_declaration.entity_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of the **entity** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         entity fifo is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       entity fifo is
    """

    def __init__(self):
        super().__init__(lTokens)
