# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)


class rule_300(token_indent):
    """
    This rule checks the indent of the **procedure** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         procedure my_proc is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       library ieee;

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
