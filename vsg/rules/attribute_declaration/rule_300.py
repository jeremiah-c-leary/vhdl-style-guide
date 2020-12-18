
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.attribute_declaration.attribute_keyword)


class rule_300(token_indent):
    '''
    Checks for indent of the *attribute* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'attribute_declaration', '300', lTokens)
