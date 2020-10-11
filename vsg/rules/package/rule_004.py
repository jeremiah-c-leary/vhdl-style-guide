
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_004(token_case):
    '''
    Checks the "package" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '004', lTokens)
