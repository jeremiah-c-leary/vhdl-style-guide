
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.package_body.package_simple_name)
lTokens.append(token.package_body.end_package_simple_name)


class rule_600(token_suffix):
    '''
    Constant rule 600 checks for suffixes in package identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'package_body', '600', lTokens)
        self.suffixes = ['_pkg']
