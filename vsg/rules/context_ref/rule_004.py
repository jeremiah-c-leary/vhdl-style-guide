
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_reference.selected_name)


class rule_004(token_case_with_prefix_suffix):
    '''
    Checks the context selected names have proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context_ref', '004', lTokens)
