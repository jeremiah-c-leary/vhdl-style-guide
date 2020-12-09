
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.is_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the package keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'package_body', '201', lTokens)
