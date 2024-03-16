# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.signal_declaration.assignment_operator)


class rule_101(Rule):
    """
    This rule checks for a single space before the default assignment token.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic      := '0';
       signal rd_en : std_logic:= '1';

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic      := '0';
       signal rd_en : std_logic := '1';
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = ">=1"
