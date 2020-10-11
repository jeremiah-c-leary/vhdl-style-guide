
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_015(token_indent):
    '''
    Checks for indent of the *end* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'package', '015', lTokens)
