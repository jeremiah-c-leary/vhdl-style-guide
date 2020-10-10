
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_008(token_case):
    '''
    Checks the instance label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'instantiation', '008', lTokens)
