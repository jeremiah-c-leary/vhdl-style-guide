
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.entity_simple_name)


class rule_012(token_case):
    '''
    Checks the entity_simple_name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '012', lTokens)
