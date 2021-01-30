
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_204(previous_line):
    '''
    Checks for a blank line above the end keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'block', '204', lTokens)
