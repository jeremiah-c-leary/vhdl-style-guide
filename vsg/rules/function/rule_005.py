
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.function_specification.function_keyword)


class rule_005(token_case):
    '''
    Checks the "function" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '005', lTokens)
