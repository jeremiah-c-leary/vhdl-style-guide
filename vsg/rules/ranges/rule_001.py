
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.direction.downto)


class rule_001(token_case):
    '''
    Checks the "downto" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'range', '001', lTokens)
