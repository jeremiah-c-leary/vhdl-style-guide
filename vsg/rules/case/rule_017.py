
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.end_keyword)


class rule_017(token_case):
    '''
    Case rule 017 checks the *end* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '017', lTokens)
