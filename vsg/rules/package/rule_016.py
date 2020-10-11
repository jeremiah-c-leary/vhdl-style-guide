
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_016(token_suffix):
    '''
    Constant rule 016 checks for suffixes in package identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'package', '016', lTokens)
        self.suffixes = ['_pkg']
