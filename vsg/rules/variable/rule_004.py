
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_004(token_case):
    '''
    Checks the variable identifiers have proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'variable', '004', lTokens)
