
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.of_keyword)


class rule_502(token_case):
    '''
    Checks the of keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute_specification', '502', lTokens)
