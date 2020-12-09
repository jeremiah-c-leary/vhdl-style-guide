
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.semicolon)


class rule_203(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line after the closing of the package body.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'package_body', '203', lTokens)
