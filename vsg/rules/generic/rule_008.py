
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_008(token_indent):
    '''
    Generic rule 008 checks the indentation of closing parenthesis for generic maps.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generic', '008', lTokens)
