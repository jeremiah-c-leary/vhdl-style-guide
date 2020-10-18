
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_002(token_case):
    '''
    Checks the "type" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'type', '002', lTokens)
