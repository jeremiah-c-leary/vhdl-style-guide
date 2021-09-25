
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)


class rule_505(token_case):
    '''
    Checks the procedure end procedure keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '505', lTokens)
