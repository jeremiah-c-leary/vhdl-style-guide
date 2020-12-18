
from vsg import token

from vsg.rules import single_space_before_token

lTokens = []
lTokens.append(token.attribute_specification.is_keyword)


class rule_101(single_space_before_token):
    '''
    Checks for a single spaces between keywords.
    '''
    def __init__(self):
        single_space_before_token.__init__(self, 'attribute_specification', '101', lTokens)
