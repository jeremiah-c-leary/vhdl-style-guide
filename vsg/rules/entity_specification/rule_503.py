
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_specification.entity_class)


class rule_503(token_case):
    '''
    Checks the *all* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity_specification', '503', lTokens)
