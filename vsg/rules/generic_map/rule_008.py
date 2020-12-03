
from vsg import token

from vsg.rules import formal_part_in_association_element_between_tokens

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis


class rule_008(formal_part_in_association_element_between_tokens):
    '''
    Checks for formal_part in port map aspects.
    '''
    def __init__(self):
        formal_part_in_association_element_between_tokens.__init__(self, 'generic_map', '008', lStart, lEnd)
        self.solution = 'Add formal_part to positional assignment.'
