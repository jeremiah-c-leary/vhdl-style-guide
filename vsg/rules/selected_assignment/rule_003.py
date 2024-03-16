# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import remove_carriage_return_after_token as Rule

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.select_keyword)
lTokens.append(token.selected_force_assignment.select_keyword)
lTokens.append(token.selected_variable_assignment.select_keyword)
lTokens.append(token.selected_waveform_assignment.select_keyword)


class rule_003(Rule):
    """
    This rule checks the **select** keyword is on the same line as the target.

    **Violation**

    .. code-block:: vhdl

       with mux_sel select
         addr <=
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
        super().__init__(lTokens, bInsertSpace=True)
        self.solution = "Removed carraige returns after with keyword"
