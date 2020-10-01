
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_context_keyword)


class rule_015(token_case):
    '''
    Checks the end context keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '015', lTokens)
