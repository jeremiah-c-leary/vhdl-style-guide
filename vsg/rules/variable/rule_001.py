
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.shared_keyword)
lTokens.append(token.variable_declaration.variable_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of a variable declaration.
    '''

    def __init__(self):
        token_indent.__init__(self, 'variable', '001', lTokens)
