
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_600(token_suffix):
    '''
    Checks for suffixes in instantiation labels.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'instantiation', '600', lTokens)
        self.suffixes = ['_inst']
