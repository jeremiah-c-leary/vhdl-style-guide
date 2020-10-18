
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_004(token_case):
    '''
    Checks the identifier has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'type', '004', lTokens)
