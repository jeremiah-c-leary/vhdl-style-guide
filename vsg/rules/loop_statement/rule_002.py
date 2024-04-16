# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_002(split_line_at_token):
    """
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       loop
         a <= b; end loop;

    **Fix**

    .. code-block:: vhdl

       loop
         a <= b;
       end loop;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *end* keyword to the next line."
