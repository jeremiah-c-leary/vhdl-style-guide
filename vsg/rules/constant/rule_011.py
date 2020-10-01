
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.subtype_indication)


class rule_011(token_case):
    '''
    Constant rule 011 checks the constant type has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'constant', '011', lTokens)
