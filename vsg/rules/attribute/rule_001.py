
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.attribute_declaration.attribute_keyword)
lTokens.append(token.attribute_specification.attribute_keyword)

class rule_001(token_indent):
    '''
    Attribute rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'attribute', '001', lTokens)
