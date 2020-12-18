
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.is_keyword)


class rule_503(token_case):
    '''
    Checks the is keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute_specification', '503', lTokens)
