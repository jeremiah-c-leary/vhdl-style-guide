
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_keyword)


class rule_202(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the package keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'package_body', '202', lTokens)
