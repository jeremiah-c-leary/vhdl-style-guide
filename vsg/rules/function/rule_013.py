
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)


class rule_013(token_case):
    '''
    Checks the *end* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'function', '013', lTokens)
