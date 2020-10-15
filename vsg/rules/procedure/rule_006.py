
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.close_parenthesis)


class rule_006(token_indent):
    '''
    Checks the indent of the closing parenthesis of the parameter list if it is on it's own line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure', '006', lTokens)
