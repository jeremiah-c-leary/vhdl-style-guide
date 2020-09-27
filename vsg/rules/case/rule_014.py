
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.case_keyword)


class rule_014(token_case):
    '''
    Case rule 014 checks the *case* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '014', lTokens)
