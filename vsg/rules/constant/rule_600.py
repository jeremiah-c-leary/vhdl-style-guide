
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_600(token_suffix):
    '''
    Constant rule 600 checks for suffixes in constant identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'constant', '600', lTokens)
        self.suffixes = ['_c']
