# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.label_name)
lTokens.append(token.procedure_call_statement.label)


class rule_300(token_indent):
    """
    This rule checks the indent of the procedure_call label.

    **Violation**

    .. code-block:: vhdl

       a <= b;

         procedure_label : WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       a <= b;

       procedure_label : WR_EN(parameter);
    """

    def __init__(self):
        super().__init__(lTokens)
