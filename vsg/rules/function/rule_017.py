
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.function_specification.designator)


class rule_017(token_case):
    '''
    Checks the function designator has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '017', lTokens)
