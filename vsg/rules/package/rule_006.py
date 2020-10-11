
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_006(token_case):
    '''
    Checks the "end" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'package', '006', lTokens)
