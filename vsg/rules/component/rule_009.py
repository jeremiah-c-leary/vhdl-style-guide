
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_009(token_indent):
    '''
    Component rule 009 checks for spaces before the "end" keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'component', '009', lTokens)
