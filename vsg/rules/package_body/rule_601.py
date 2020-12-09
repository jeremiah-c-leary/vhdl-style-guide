
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.package_body.package_simple_name)
lTokens.append(token.package_body.end_package_simple_name)


class rule_601(token_prefix):
    '''
    Constant rule 601 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'package_body', '601', lTokens)
        self.prefixes = ['pkg_']
        self.solution = 'Package identifier'
