
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_500(token_case):
    '''
    Checks the block label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '500', lTokens)
