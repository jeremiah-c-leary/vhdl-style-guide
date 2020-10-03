
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.identifier)


class rule_008(token_case):
    '''
    Checks the "is" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '008', lTokens)
