
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.simple_variable_assignment.assignment, token.simple_variable_assignment.semicolon])
lTokenPairs.append([token.conditional_variable_assignment.assignment, token.conditional_variable_assignment.semicolon])


class rule_004(multiline_alignment_between_tokens):
    '''
    This rule checks the alignment of multiline variable assignments.

    **Violation**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
              30 + 35;

    **Fix**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
                    30 + 35;
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'variable_assignment', '004', lTokenPairs)
        self.phase = 5
        self.subphase = 2
