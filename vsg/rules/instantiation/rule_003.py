
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.component_instantiation_statement.instantiation_label, token.component_instantiation_statement.label_colon])


class rule_003(single_space_between_token_pairs):
    '''
    Checks for a single space before the :
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'instantiation', '003', lTokens)
        self.solution = 'Ensure only one space before the :.'
