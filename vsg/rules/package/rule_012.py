
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_012(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "end package" keywords.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'package', '012', lTokens)
