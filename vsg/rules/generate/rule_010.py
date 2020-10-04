
from vsg import token

from vsg.rules import token_case

lTokens = []
lTokens.append(token.case_generate_statement.end_generate_keyword)
lTokens.append(token.for_generate_statement.end_generate_keyword)
lTokens.append(token.if_generate_statement.end_generate_keyword)


class rule_010(token_case):
    '''
    Checks the *generate* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'generate', '010', lTokens)
