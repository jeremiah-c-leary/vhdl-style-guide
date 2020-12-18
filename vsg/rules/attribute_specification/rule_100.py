
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.attribute_specification.attribute_keyword)
lTokens.append(token.attribute_specification.attribute_designator)
lTokens.append(token.attribute_specification.of_keyword)
lTokens.append(token.attribute_specification.is_keyword)


class rule_100(single_space_after_token):
    '''
    Checks for a single spaces between keywords.
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'attribute_specification', '100', lTokens)
