
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_kind.function_keyword)


class rule_014(token_case):
    '''
    Checks the "function" keyword in the "end function" has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '014', lTokens)
