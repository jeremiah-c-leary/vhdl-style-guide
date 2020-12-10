
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_301(token_indent):
    '''
    Checks for indent of the block label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'block', '301', lTokens)
