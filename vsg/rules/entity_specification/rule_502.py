
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.entity_designator.entity_tag)


class rule_502(token_case_with_prefix_suffix):
    '''
    Checks the *all* keyword has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'entity_specification', '502', lTokens)
