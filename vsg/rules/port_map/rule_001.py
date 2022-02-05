
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.port_map_aspect.port_keyword)
lTokens.append(token.port_map_aspect.map_keyword)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_001(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the **port map** keywords have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PORT MAP (

    **Fix**

    .. code-block:: vhdl

       port map (
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'port_map', '001', lTokens, oStart, oEnd)
        self.groups.append('case::keyword')
