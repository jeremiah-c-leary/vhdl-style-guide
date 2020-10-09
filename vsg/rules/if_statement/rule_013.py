
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)


class rule_013(token_indent):
    '''
    Checks the indent of the "else" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'if', '013', lTokens)
