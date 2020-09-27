
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.is_keyword)


class rule_015(token_case):
    '''
    Case rule 015 checks the *case* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '015', lTokens)
