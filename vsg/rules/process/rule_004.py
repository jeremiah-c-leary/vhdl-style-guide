
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_004(token_case):
    '''
    Checks the *begin* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '004', lTokens)
