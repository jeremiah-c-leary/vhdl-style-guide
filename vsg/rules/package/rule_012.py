
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_012(previous_line):
    '''
    Checks for a blank line above the "end package" keywords.
    '''

    def __init__(self):
        previous_line.__init__(self, 'package', '012', lTokens)
