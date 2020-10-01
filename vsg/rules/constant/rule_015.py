
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_015(token_prefix):
    '''
    Constant rule 015 checks for prefixes in constant identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'constant', '015', lTokens)
        self.prefixes = ['c_']
