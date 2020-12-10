
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_keyword)


class rule_501(token_case):
    '''
    Checks the block keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '501', lTokens)
