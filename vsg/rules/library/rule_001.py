
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_001(token_indent):
    '''
    Checks for indent of the *library* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'library', '001', lTokens)
