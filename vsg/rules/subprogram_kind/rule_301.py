# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.subprogram_kind.function_keyword)


class rule_301(token_indent):
    """
    This rule checks the indent of the **function** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         function my_func is new my_generic_func

    **Fix**

    .. code-block:: vhdl

       library ieee;

       function my_func is new my_generic_func
    """

    def __init__(self):
        super().__init__(lTokens)
