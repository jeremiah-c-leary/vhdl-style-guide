
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_009(token_indent):
    '''
    Checks for indent of the end keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'entity', '009', lTokens)
