
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_010(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the port names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en     : in    std_logic;
         rd_en     : in    std_logic;
         OVERFLOW  : out   std_logic;
         underflow : out   std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         wr_en     : in    std_logic;
         rd_en     : in    std_logic;
         overflow  : out   std_logic;
         underflow : out   std_logic
       );
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'port', '010', lTokens, token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.configuration.append('prefix_exceptions')
        self.configuration.append('suffix_exceptions')
        self.configuration.append('case_exceptions')
        self.groups.append('case::name')
