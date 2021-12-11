
from vsg.rules import token_case_with_prefix_suffix

from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.identifier)


class rule_013(token_case_with_prefix_suffix):
    '''
    Entity rule 013 checks the architecture identifier has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'architecture', '013', lTokens)
