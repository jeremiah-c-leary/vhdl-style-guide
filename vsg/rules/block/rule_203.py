
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_203(blank_line_below_line_ending_with_token):
    '''
    Checks for a blank line below the package keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'block', '203', lTokens)
