
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.identifier)


class rule_012(token_case_with_prefix_suffix):
    '''
    Checks the context identifier has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context', '012', lTokens)
