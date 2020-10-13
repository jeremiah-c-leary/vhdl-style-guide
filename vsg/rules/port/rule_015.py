
from vsg import token

from vsg.rules import token_indent

lTokens = []
lTokens.append(token.port_clause.close_parenthesis)


class rule_015(token_indent):
    '''
    Checks the indentation of closing parenthesis for port maps.
    '''

    def __init__(self):
        token_indent.__init__(self, 'port', '015', lTokens)
