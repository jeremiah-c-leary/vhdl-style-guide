
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_010(token_case):
    '''
    Component rule 010 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '010', lTokens)
