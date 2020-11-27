
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.if_statement.if_keyword, token.if_statement.then_keyword])
lTokenPairs.append([token.if_statement.elsif_keyword, token.if_statement.then_keyword])


class rule_009(multiline_alignment_between_tokens):
    '''
    Checks the alignment of multiline if signal assignments.
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'if', '009', lTokenPairs)
        self.phase = 4
        self.subphase = 2
