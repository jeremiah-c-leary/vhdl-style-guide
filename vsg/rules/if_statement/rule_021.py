# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.if_statement.else_keyword)


class rule_021(split_line_at_token):
    """
    This rule checks the **else** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       if (a = '1') then c <= '1'; else c <= '0'; end if;

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then c <= '0';
       else c <= '1'; end if;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *else* keyword to its own line."
