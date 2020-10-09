
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)


class rule_027(token_case):
    '''
    Checks the "else" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '027', lTokens)
