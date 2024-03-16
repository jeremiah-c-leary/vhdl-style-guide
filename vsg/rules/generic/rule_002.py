# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.generic_clause.generic_keyword)


class rule_002(token_indent):
    """
    This rule checks the indent of the **generic** keyword.

    **Violation**

    .. code-block:: vhdl

       entity fifo is
            generic (

       entity fifo is
       generic (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         generic (

       entity fifo is
         generic (
    """

    def __init__(self):
        super().__init__(lTokens)
