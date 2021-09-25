
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.function_specification.close_parenthesis)


class rule_300(token_indent):
    '''
    Checks the indent of the closing parenthesis of the parameter list if it is on it's own line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'function', '300', lTokens)
