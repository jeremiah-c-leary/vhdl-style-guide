
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)


class rule_506(token_case):
    '''
    Checks the function designator in the end procedure has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '506', lTokens)
