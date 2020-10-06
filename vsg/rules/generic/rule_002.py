
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.generic_keyword)


class rule_002(token_indent):
    '''
    Checks indentation of the "generic" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generic', '002', lTokens)
