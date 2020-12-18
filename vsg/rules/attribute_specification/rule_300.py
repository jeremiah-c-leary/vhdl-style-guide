
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.attribute_keyword)


class rule_300(token_indent):
    '''
    Checks for indent of the attribute_specification label.
    '''

    def __init__(self):
        token_indent.__init__(self, 'attribute_specification', '300', lTokens)
