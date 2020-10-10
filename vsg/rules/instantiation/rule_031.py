
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.component_keyword)


class rule_031(token_case):
    '''
    Checks the **component** keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '031', lTokens)
