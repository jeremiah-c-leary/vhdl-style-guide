# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules import multiline_array_alignment as Rule

lTokenPairs = []
lTokenPairs.append([token.simple_waveform_assignment.assignment, token.simple_waveform_assignment.semicolon])


class rule_402(Rule):
    """
    This rule checks the alignment of multiline simple sequential signal assignments that contain arrays.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_data <=
       (
                0,
            65535,
            32768
         );

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
        self.assignment_operator = token.simple_waveform_assignment.assignment
