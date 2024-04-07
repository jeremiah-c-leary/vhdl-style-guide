# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.simple_variable_assignment.assignment, token.simple_variable_assignment.semicolon])


class rule_008(Rule):
    """
    This rule checks the structure of multiline variable assignments that contain arrays.

    |configuring_array_multiline_structure_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_data := (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       wr_data :=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.assignment_operator = token.simple_variable_assignment.assignment
        self.semicolon = token.simple_variable_assignment.semicolon
