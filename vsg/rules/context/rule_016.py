
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_simple_name)


class rule_016(token_case):
    '''
    Checks the context_simple_name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '016', lTokens)
