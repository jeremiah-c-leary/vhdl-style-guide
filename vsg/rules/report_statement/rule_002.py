# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token_when_between_tokens

lTokens = []
lTokens.append(token.report_statement.severity_keyword)

oStart = token.report_statement.report_keyword
oEnd = token.report_statement.semicolon


class rule_002(split_line_at_token_when_between_tokens):
    """
    This rule checks the **severity** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits." severity FAILURE;

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.solution = "Place **severity** keyword on its own line."
