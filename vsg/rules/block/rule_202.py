
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)

lAllowTokens = []
lAllowTokens.append(token.block_statement.is_keyword)
lAllowTokens.append(token.block_statement.guard_close_parenthesis)


class rule_202(previous_line):
    '''
    Checks for a blank line above the block label.
    '''

    def __init__(self):
        previous_line.__init__(self, 'block', '202', lTokens, lAllowTokens)
