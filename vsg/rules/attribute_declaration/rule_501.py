
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.attribute_declaration.identifier)


class rule_501(token_case_with_prefix_suffix):
    '''
    Checks the identifier has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'attribute_declaration', '501', lTokens)
