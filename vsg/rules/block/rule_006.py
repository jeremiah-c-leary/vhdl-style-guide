# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_006(split_line_at_token):
    """
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       a <= b; end block;

    **Fix**

    .. code-block:: vhdl

       a <= b;
       end block;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *end* keyword and code after it to the next line"
