# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.selected_force_assignment.force_keyword)


class rule_105(Rule):
    """
    This rule checks for a single space after the **force** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <= force   "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <= force "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens)
