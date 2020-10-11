
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_package_keyword)


class rule_018(token_case):
    '''
    Checks the "package" keyword in the "end package" has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '018', lTokens)
