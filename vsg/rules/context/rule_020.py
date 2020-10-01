
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_020(token_indent):
    '''
    Checks for indent on the end keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'context', '020', lTokens)
