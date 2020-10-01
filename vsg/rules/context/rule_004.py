
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_keyword)


class rule_004(token_case):
    '''
    Checks the "context" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '004', lTokens)
