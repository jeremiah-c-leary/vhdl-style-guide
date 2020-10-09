
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_012(token_indent):
    '''
    Checks the indent of the "elsif" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'if', '012', lTokens)
