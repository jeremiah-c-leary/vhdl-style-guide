
from vsg.rules import token_case_first_token_after_token

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_010(token_case_first_token_after_token):
    '''
    Checks the variable type has proper case.
    '''

    def __init__(self):
        token_case_first_token_after_token.__init__(self, 'variable', '010', lTokens)
