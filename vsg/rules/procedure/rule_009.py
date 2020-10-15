
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)


class rule_009(token_case):
    '''
    Checks the *procedure* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '009', lTokens)
