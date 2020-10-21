
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.direction.to)


class rule_002(token_case):
    '''
    Checks the "to" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'range', '002', lTokens)
