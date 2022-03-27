
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_file_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_007(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the generic names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       G_WIDTH : integer := 32;

    **Fix**

    .. code-block:: vhdl

       g_width : integer := 32;
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'generic', '007', lTokens, oStart, oEnd)
        self.configuration.append('prefix_exceptions')
        self.configuration.append('suffix_exceptions')
        self.configuration.append('case_exceptions')
        self.groups.append('case::name')
