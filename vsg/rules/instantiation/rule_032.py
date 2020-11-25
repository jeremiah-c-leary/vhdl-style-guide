
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.instantiated_unit.component_keyword, token.instantiated_unit.component_name])


class rule_032(single_space_between_token_pairs):
    '''
   Checks for a single space between the *component* keyword and the entity_name.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'instantiation', '032', lTokens)
        self.solution = 'Ensure a single space exists between *component* and the component_name.'
