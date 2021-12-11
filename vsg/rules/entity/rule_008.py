
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.identifier)


class rule_008(token_case_with_prefix_suffix):
    '''
    Checks the "is" keyword has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'entity', '008', lTokens)
