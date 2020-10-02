
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_001(token_indent):
    '''
    Checks for indent on the context reference keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'context_ref', '001', lTokens)
