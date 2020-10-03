
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.entity_keyword)


class rule_004(token_case):
    '''
    Checks the "entity" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '004', lTokens)
