
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.designator)


class rule_506(token_case):
    '''
    Checks the procedure end procedure name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '506', lTokens)
