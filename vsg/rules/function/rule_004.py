
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)


class rule_004(token_case):
    '''
    Checks the "entity" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '004', lTokens)
