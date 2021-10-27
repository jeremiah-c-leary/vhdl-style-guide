
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_simple_name)


class rule_016(token_case_with_prefix_suffix):
    '''
    Checks the context_simple_name has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context', '016', lTokens)
