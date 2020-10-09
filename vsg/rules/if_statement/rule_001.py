
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.if_statement.if_keyword)


class rule_001(token_indent):
    '''
    Checks the indent of the "if" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'if', '001', lTokens)
