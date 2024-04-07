# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_004(split_line_at_token):
    """
    This rule checks the **begin** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       block is begin

    **Fix**

    .. code-block:: vhdl

       block is
       begin
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *begin* keyword and code after it to the next line"
