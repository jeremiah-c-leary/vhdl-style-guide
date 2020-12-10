
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_504(token_case):
    '''
    Checks the end keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '504', lTokens)
