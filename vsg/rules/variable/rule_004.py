
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    '''
    Checks the variable identifiers have proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'variable', '004', lTokens)
