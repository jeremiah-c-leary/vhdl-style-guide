
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_200(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the block label.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'block', '200', lTokens)
