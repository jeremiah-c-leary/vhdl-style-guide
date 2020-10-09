
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.if_statement.end_keyword)


class rule_014(token_indent):
    '''
    Checks the indent of the "end" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'if', '014', lTokens)
