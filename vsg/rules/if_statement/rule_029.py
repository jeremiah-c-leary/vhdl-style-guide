
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.then_keyword)


class rule_029(token_case):
    '''
    Checks the *then* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '029', lTokens)
