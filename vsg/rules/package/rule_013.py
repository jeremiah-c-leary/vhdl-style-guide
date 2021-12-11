
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.is_keyword)


class rule_013(token_case_with_prefix_suffix):
    '''
    Checks the "is" keyword has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '013', lTokens)
