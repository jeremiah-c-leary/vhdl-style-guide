
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_503(token_case):
    '''
    Checks the begin keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '503', lTokens)
