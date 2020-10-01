
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.constant_keyword)


class rule_002(token_case):
    '''
    Constant rule 002 checks the "constant" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'constant', '002', lTokens)
