
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_package_simple_name)


class rule_507(token_case_with_prefix_suffix):
    '''
    Checks the "body" keyword has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'package_body', '507', lTokens)
