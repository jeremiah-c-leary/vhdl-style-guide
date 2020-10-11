
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_010(token_case):
    '''
    Checks the package name has proper case in the package declaration.
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '010', lTokens)
