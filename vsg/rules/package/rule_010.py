
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_010(token_case_with_prefix_suffix):
    '''
    Checks the package name has proper case in the package declaration.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '010', lTokens)
