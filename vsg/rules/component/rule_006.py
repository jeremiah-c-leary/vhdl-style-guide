
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.is_keyword)


class rule_006(token_case):
    '''
    Component rule 006 checks the is keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '006', lTokens)
