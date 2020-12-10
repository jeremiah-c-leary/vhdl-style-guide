
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_label)


class rule_506(token_case):
    '''
    Checks the block keyword in the end statement has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '506', lTokens)
