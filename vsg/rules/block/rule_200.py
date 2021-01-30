
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_200(previous_line):
    '''
    Checks for a blank line above the block label.
    '''

    def __init__(self):
        previous_line.__init__(self, 'block', '200', lTokens)
