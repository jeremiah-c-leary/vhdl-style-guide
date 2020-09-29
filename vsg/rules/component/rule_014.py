
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_component_keyword)


class rule_014(token_case):
    '''
    Component rule 014 checks the is keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '014', lTokens)
