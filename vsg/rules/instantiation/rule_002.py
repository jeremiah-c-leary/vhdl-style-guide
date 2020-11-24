
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.component_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.entity_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.configuration_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.component_name])


class rule_002(single_space_between_token_pairs):
    '''
    Checks for a single space after the :
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'instantiation', '002', lTokens)
        self.solution = 'Ensure only one space after the :.'
