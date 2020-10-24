
from vsg import parser
from vsg import token

from vsg.rules import token_case_formal_part_of_association_element_in_map_between_tokens

oStart = token.component_instantiation_statement.instantiation_label
oEnd = token.component_instantiation_statement.semicolon

sMapType = 'generic'


class rule_016(token_case_formal_part_of_association_element_in_map_between_tokens):
    '''
    Checks the generic name has proper case.
    '''
    def __init__(self):
        token_case_formal_part_of_association_element_in_map_between_tokens.__init__(self, 'instantiation', '016', sMapType, oStart, oEnd)
