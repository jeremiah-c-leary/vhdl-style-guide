
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.is_keyword)


class rule_502(token_case):
    '''
    Checks the block label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '502', lTokens)
