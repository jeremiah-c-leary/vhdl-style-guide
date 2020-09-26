
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.attribute_keyword)
lTokens.append(token.attribute_declaration.attribute_keyword)

class rule_002(token_case):
    '''
    Attribute rule 002 checks the attribute keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute', '002', lTokens)
