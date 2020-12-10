
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_keyword)


class rule_505(token_case):
    '''
    Checks the block keyword in the end statement has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '505', lTokens)
