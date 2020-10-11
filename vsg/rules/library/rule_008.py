
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_008(token_indent):
    '''
    Checks for indent of the *use* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'library', '008', lTokens)
