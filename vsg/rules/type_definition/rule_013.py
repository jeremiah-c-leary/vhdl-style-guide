
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.full_type_declaration.is_keyword)


class rule_013(token_case):
    '''
    Checks the *is* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'type', '013', lTokens)
