
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_501(token_case):
    '''
    Checks the procedure designator has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '501', lTokens)
