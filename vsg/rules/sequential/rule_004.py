# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_alignment_between_tokens

lTokenPairs = []
lTokenPairs.append([token.simple_waveform_assignment.assignment, token.simple_waveform_assignment.semicolon])
lTokenPairs.append([token.simple_force_assignment.assignment, token.simple_force_assignment.semicolon])
lTokenPairs.append([token.conditional_waveform_assignment.assignment, token.conditional_waveform_assignment.semicolon])
lTokenPairs.append([token.conditional_force_assignment.assignment, token.conditional_force_assignment.semicolon])


class rule_004(multiline_alignment_between_tokens):
    """
    This rule checks the alignment of multiline sequential statements.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       overflow <= wr_en and
         rd_en;

    **Fix**

    .. code-block:: vhdl

       overflow <= wr_en and
                   rd_en;
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.phase = 5
        self.subphase = 2
