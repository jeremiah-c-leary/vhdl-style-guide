
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_package_simple_name)


class rule_008(token_case):
    '''
    Checks the package name has proper case on the closing "end package" line.
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '008', lTokens)
