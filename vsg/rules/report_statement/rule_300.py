# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.report_statement.report_keyword)
lTokens.append(token.report_statement.severity_keyword)


class rule_300(token_indent):
    """
    This rule checks indent of multiline report statements.

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
                severity FAILURE;

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens)
