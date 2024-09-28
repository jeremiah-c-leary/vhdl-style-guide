# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_023(split_line_at_token):
    """
    This rule checks the **elsif** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       if (a = '1') then c <= '1'; else c <= '0'; elsif (b = '0') then d <= '0'; end if;

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then c <= '1'; else c <= '0';
       elsif (b = '0') then d <= '0'; end if;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *elsif* keyword to its own line."
