
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    '''
    Constant rule 004 checks the constant names have proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'constant', '004', lTokens)
