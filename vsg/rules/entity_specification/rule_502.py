
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_designator.entity_tag)


class rule_502(token_case):
    '''
    Checks the *all* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity_specification', '502', lTokens)
