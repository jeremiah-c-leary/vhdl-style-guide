
from vsg import parser

from vsg.token import constant_declaration

from vsg.rules import token_indent_unless_between_tokens

lTokens = []
lTokens.append(parser.comment)

lUnless = []
lUnless.append([constant_declaration.constant_keyword, constant_declaration.semicolon])


class rule_010(token_indent_unless_between_tokens):
    '''
    Comment rule 010 checks for the proper indent of comments.
    '''

    def __init__(self):
        token_indent_unless_between_tokens.__init__(self, 'comment', '010', lTokens, lUnless)
        self.phase = 4
        self.subphase = 3
