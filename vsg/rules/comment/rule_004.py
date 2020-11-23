
from vsg import parser

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(parser.comment)


class rule_004(whitespace_before_token):
    '''
    Comment rule 004 ensures there is at least one space before comments on a line with code.
    '''

    def __init__(self):
        whitespace_before_token.__init__(self, 'comment', '004', lTokens)
        self.solution = 'Add a single space before comment'
