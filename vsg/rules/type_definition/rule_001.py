
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the type statement.
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '001', lTokens)
