
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_reference.selected_name)


class rule_004(token_case):
    '''
    Checks the context selected names have proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context_ref', '004', lTokens)
