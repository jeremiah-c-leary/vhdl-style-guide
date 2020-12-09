
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.package_body.package_keyword)


class rule_500(token_case):
    '''
    Checks the "package" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'package_body', '500', lTokens)
