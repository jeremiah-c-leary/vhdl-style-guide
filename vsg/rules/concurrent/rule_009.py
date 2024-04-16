# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_conditional_alignment as Rule

lTokenPairs = []
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_009(Rule):
    """
    This rule checks alignment of multiline concurrent conditional signal statements.

    |configuring_conditional_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else
            '1';

       w_foo <= I_FOO when ((I_BAR = '1') and
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
