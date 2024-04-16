# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])


class rule_012(Rule):
    """
    This rule checks the structure of multiline concurrent simple signal assignments that contain arrays.

    |configuring_array_multiline_structure_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_data <= (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       wr_data <=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.assignment_operator = token.concurrent_simple_signal_assignment.assignment
        self.semicolon = token.concurrent_simple_signal_assignment.semicolon
