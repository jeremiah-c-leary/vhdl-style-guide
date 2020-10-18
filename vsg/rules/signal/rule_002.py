
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.signal_keyword)


class rule_002(token_case):
    '''
    Checks the "signal" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'signal', '002', lTokens)
