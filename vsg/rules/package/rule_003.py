
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_003(previous_line):
    '''
    Checks for a blank line above the package keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'package', '003', lTokens)
        self.style = 'no_code'
