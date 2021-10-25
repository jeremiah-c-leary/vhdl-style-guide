
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.component_simple_name)


class rule_012(token_case_with_prefix_suffix):
    '''
    Component rule 012 checks component simple name has proper case in "end" keyword line.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'component', '012', lTokens)
