
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_keyword)


class rule_301(token_indent):
    '''
    Checks for indent of the *end* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'package_body', '301', lTokens)
