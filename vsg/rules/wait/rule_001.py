
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.wait_statement.wait_keyword)
lTokens.append(token.wait_statement.label)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'wait', '001', lTokens)
