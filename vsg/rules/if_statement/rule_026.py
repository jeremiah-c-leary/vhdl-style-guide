
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_026(token_case):
    '''
    Checks the "elsif" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '026', lTokens)
