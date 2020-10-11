
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_005(token_case):
    '''
    Checks the *use* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'library', '005', lTokens)
