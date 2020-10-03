
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_010(token_case):
    '''
    Checks the end keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '010', lTokens)
