# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_simple_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.simple_variable_assignment.assignment, token.simple_variable_assignment.semicolon])
lTokenPairs.append([token.conditional_variable_assignment.assignment, token.conditional_variable_assignment.semicolon])


class rule_007(Rule):
    """
    This rule checks the structure of simple and conditional variable assignments.

    |configuring_simple_multiline_structure_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en :=
         '0' when q_wr_en = '1' else
                '1';

       w_foo :=
         I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';

    **Fix**

    .. code-block:: vhdl

       wr_en := '0' when q_wr_en = '1' else
                '1';

       w_foo := I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';
    """

    def __init__(self):
        super().__init__(lTokenPairs)
