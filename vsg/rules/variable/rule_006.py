
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_006(whitespace_before_token):
    '''
    Checks there is at least a single space before the colon.
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'variable', '006', lTokens)
        self.solution = 'Ensure at least a single space exists before the :'
