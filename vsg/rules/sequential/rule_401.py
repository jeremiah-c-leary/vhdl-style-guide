# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_conditional_alignment as Rule

lTokenPairs = []
lTokenPairs.append([token.conditional_waveform_assignment.assignment, token.conditional_waveform_assignment.semicolon])


class rule_401(Rule):
    """
    This rule checks alignment of multiline sequential conditional signal assignments.

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
