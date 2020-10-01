
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_014(token_case):
    '''
    Checks the is keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '014', lTokens)
