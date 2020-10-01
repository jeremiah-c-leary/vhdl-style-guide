
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.identifier)


class rule_012(token_case):
    '''
    Checks the context identifier has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '012', lTokens)
