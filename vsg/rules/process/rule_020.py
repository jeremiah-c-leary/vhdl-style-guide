
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])


class rule_020(multiline_alignment_between_tokens):
    '''
    Checks the alignment of multiline sensitivity lists.
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'process', '020', lTokenPairs, True)
