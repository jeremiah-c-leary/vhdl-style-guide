# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.procedure_call.procedure_name)


class rule_302(token_indent):
    """
    This rule checks the indent of the *procedure* name.

    **Violation**

    .. code-block:: vhdl

       a <= b;

         WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       a <= b;

       WR_EN(parameter);
    """

    def __init__(self):
        super().__init__(lTokens)
