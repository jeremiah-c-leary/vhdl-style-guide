
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_001(token_indent):
    '''
    Checks for indent of the *package* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'package', '001', lTokens)
