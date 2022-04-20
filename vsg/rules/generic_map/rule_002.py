
from vsg import token

from vsg.rules import token_case_formal_part_of_association_element_in_map_between_tokens

oStart = token.component_instantiation_statement.instantiation_label
oEnd = token.component_instantiation_statement.semicolon

sMapType = 'generic'


class rule_002(token_case_formal_part_of_association_element_in_map_between_tokens):
    '''
    This rule checks generic names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         generic map (
           DEPTH => 512,
           WIDTH => 32
         )

    **Fix**

    .. code-block:: vhdl

         generic map (
           depth => 512,
           width => 32
         )
    '''
    def __init__(self):
        token_case_formal_part_of_association_element_in_map_between_tokens.__init__(self, 'generic_map', '002', sMapType, oStart, oEnd)
        self.configuration.append('prefix_exceptions')
        self.configuration.append('suffix_exceptions')
        self.configuration.append('case_exceptions')
        self.groups.append('case::name')
