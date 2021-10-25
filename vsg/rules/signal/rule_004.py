
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    '''
    Checks the signal identifier has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'signal', '004', lTokens)
