
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_package_keyword)


class rule_018(token_case_with_prefix_suffix):
    '''
    Checks the "package" keyword in the "end package" has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '018', lTokens)
