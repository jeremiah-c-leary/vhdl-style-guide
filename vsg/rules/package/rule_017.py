
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_017(token_prefix):
    '''
    Constant rule 017 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'package', '017', lTokens)
        self.prefixes = ['pkg_']
        self.solution = 'Package identifier'
