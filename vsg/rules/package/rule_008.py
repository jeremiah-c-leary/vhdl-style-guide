
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_package_simple_name)


class rule_008(token_case_with_prefix_suffix):
    '''
    Checks the package name has proper case on the closing "end package" line.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package', '008', lTokens)
