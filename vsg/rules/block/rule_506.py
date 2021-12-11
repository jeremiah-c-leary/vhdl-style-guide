
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_label)


class rule_506(token_case_with_prefix_suffix):
    '''
    Checks the block keyword in the end statement has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'block', '506', lTokens)
