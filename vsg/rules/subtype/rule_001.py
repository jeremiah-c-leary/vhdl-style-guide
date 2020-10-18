
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.subtype_declaration.subtype_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the subtype statement.
    '''

    def __init__(self):
        token_indent.__init__(self, 'subtype', '001', lTokens)
