
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_keyword)


class rule_006(token_indent):
    '''
    Checks for the proper indentation of the *end* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'process', '006', lTokens)
