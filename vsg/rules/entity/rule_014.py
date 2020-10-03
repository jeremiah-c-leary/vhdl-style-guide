
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.end_entity_keyword)


class rule_014(token_case):
    '''
    Checks the entity_simple_name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '014', lTokens)
