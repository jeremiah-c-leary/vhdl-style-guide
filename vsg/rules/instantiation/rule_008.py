
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_008(token_case_with_prefix_suffix):
    '''
    Checks the instance label has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'instantiation', '008', lTokens)
