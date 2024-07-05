# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.assertion.keyword)
lTokens.append(token.assertion.report_keyword)
lTokens.append(token.assertion.severity_keyword)
lTokens.append(token.concurrent_assertion_statement.label_name)
lTokens.append(token.assertion_statement.label)


class rule_001(token_indent):
    """
    This rule checks indent of multiline assert statements.

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
            report "FIFO width is limited to 16 bits."
        severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens)
