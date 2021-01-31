
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)

lAllowTokens = []
lAllowTokens.append(token.block_statement.is_keyword)
lAllowTokens.append(token.block_statement.guard_close_parenthesis)


class rule_202(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the block label.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'block', '202', lTokens, lAllowTokens)
