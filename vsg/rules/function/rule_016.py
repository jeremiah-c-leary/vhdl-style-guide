
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.return_statement.return_keyword)


class rule_016(token_indent):
    '''
    Checks for the proper indentation of return statements.
    '''

    def __init__(self):
        token_indent.__init__(self, 'function', '016', lTokens)
