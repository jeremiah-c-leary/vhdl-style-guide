
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.attribute_keyword)


class rule_500(token_case):
    '''
    Checks the attribute keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute_specification', '500', lTokens)
