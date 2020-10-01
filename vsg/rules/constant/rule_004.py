
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_004(token_case):
    '''
    Constant rule 004 checks the constant names have proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'constant', '004', lTokens)
