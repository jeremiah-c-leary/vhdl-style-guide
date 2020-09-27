
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.end_case_keyword)


class rule_018(token_case):
    '''
    Case rule 018 checks the case keyword has proper case in end case.
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '018', lTokens)
