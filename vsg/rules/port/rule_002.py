# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.port_clause.port_keyword)


class rule_002(token_indent):
    """
    This rule checks the indent of the **port** keyword.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
       port (

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
    """

    def __init__(self):
        super().__init__(lTokens)
