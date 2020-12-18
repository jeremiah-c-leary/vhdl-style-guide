
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.attribute_declaration.colon)


class rule_101(whitespace_before_token):
    '''
    Checks for a single space before the colon
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'attribute_declaration', '101', lTokens)
