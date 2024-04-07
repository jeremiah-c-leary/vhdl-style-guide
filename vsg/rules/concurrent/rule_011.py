# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_simple_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.assignment, token.concurrent_simple_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_011(Rule):
    """
    This rule checks the structure of simple and conditional concurrent statements.

    |configuring_simple_multiline_structure_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <=
         '0' when q_wr_en = '1' else
                '1';

       w_foo <=
         I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else
                '1';

       w_foo <= I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';
    """

    def __init__(self):
        super().__init__(lTokenPairs)
