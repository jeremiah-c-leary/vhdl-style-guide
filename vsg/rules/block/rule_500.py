
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_500(token_case_with_prefix_suffix):
    '''
    Checks the block label has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'block', '500', lTokens)
