
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.variable_keyword)


class rule_002(token_case):
    '''
    Checks the "variable" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'variable', '002', lTokens)
