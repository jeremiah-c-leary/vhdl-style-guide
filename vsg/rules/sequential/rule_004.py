
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.simple_waveform_assignment.assignment, token.simple_waveform_assignment.semicolon])
lTokenPairs.append([token.simple_force_assignment.assignment, token.simple_force_assignment.semicolon])
lTokenPairs.append([token.conditional_waveform_assignment.assignment, token.conditional_waveform_assignment.semicolon])
lTokenPairs.append([token.conditional_force_assignment.assignment, token.conditional_force_assignment.semicolon])


class rule_004(multiline_alignment_between_tokens):
    '''
    This rule checks the alignment of multiline sequential statements.

    **Violation**

    .. code-block:: vhdl

       overflow <= wr_en and
         rd_en;

    **Fix**

    .. code-block:: vhdl

       overflow <= wr_en and
                   rd_en;
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'sequential', '004', lTokenPairs)
        self.phase = 5
        self.subphase = 2
