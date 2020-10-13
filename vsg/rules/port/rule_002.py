
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.port_clause.port_keyword)


class rule_002(token_indent):
    '''
    Checks indentation of the "port" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'port', '002', lTokens)
