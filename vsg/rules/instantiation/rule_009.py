
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.component_name)


class rule_009(token_case):
    '''
    Checks the component name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '009', lTokens)
