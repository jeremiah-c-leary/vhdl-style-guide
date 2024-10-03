# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_010(split_line_at_token):
    """
    This rule checks the **library** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       context c1 is library ieee; use ieee.std_logic_1164.all; end context c1;

    **Fix**

    .. code-block:: vhdl

       context c1 is
         library ieee; use ieee.std_logic_1164.all; end context c1;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *library* to its own line."
