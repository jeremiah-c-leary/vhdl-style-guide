# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.assignment)
lTokens.append(token.selected_force_assignment.assignment)
lTokens.append(token.selected_variable_assignment.assignment)
lTokens.append(token.selected_waveform_assignment.assignment)


class rule_004(Rule):
    """
    This rule checks the assignment is on the same line as the target.

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr
         <=
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
