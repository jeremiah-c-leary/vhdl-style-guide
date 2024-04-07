# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.select_keyword)
lTokens.append(token.selected_force_assignment.select_keyword)
lTokens.append(token.selected_variable_assignment.select_keyword)
lTokens.append(token.selected_waveform_assignment.select_keyword)


class rule_501(Rule):
    """
    This rule checks the **select** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel SELECT addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
