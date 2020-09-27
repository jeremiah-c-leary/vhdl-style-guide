
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.null_statement.label)
lTokens.append(token.null_statement.null_keyword)


class rule_013(token_indent):
    '''
    Case rule 013 verifies the indent of the "Null" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'case', '013', lTokens)
