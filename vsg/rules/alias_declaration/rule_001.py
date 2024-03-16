# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token as Rule

lTokens = []
lTokens.append(token.alias_declaration.alias_keyword)


class rule_001(Rule):
    """
    This rule checks the **alias** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       signal sig1 : std_logic; alias designator is name;

    **Fix**

    .. code-block:: vhdl

       signal sig1 : std_logic;
       alias designator is name;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *alias* keyword and code after end to the next line"
