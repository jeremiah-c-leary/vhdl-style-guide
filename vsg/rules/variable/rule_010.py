
from vsg.rules import token_case_n_token_after_tokens

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_010(token_case_n_token_after_tokens):
    '''
    Checks the variable type has proper case.
    '''

    def __init__(self):
        token_case_n_token_after_tokens.__init__(self, 'variable', '010', 1, lTokens)
        self.disabled = True
