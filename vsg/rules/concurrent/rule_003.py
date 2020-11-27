
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.assignment, token.concurrent_simple_signal_assignment.semicolon])


class rule_003(multiline_alignment_between_tokens):
    '''
    Checks the alignment of multiline concurrent signal assignments.
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'concurrent', '003', lTokenPairs)
        self.phase = 5
        self.subphase = 2
