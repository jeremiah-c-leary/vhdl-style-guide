
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_body.package_keyword)


class rule_300(token_indent):
    '''
    Checks for indent of the *package* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'package_body', '300', lTokens)
