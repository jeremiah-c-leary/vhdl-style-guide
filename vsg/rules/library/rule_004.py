
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_004(token_case):
    '''
    Checks the "library" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'library', '004', lTokens)
