
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.component_name)


class rule_009(token_case_with_prefix_suffix):
    '''
    Checks the component name has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'instantiation', '009', lTokens)
