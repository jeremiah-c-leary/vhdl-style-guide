
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_003(token_indent):
    '''
    Checks for the proper indentation of the *begin* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'process', '003', lTokens)
