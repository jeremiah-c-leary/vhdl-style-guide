
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.identifier)


class rule_008(token_case):
    '''
    Component rule 008 checks the component name has proper case in the component declaration line.
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '008', lTokens)
