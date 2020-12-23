
from vsg import parser

from vsg.rules import token_indent


class rule_010(token_indent):
    '''
    Comment rule 010 checks for the proper indent of comments.
    '''

    def __init__(self):
        token_indent.__init__(self, 'comment', '010', [parser.comment])
        self.phase = 4
        self.subphase = 3
