
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.generic_keyword)


class rule_009(token_case):
    '''
    Checks the "generic" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'generic', '009', lTokens)
