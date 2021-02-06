
from vsg.rules import blank_line_below_line_ending_with_several_possible_tokens

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_keyword)
lTokens.append(token.block_statement.guard_close_parenthesis)
lTokens.append(token.block_statement.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.block_statement.begin_keyword)


class rule_201(blank_line_below_line_ending_with_several_possible_tokens):
    '''
    Checks for a blank line below the package keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_several_possible_tokens.__init__(self, 'block', '201', lTokens, lAllowTokens)
