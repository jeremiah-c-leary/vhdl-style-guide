
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_016(token_case):
    '''
    Case rule 016 checks the *when* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '016', lTokens)
