
from vsg.rules import token_prefix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_011(token_prefix_between_tokens):
    '''
    This rule checks for valid prefixes on port identifiers.
    The default port prefixes are: *i\_*, *o\_*, *io\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : in    std_logic;
         rd_en    : in    std_logic;
         overflow : out   std_logic;
         data     : inout std_logic
       );


    **Fix**

    .. code-block:: vhdl

       port (
         i_wr_en    : in    std_logic;
         i_rd_en    : in    std_logic;
         o_overflow : out   std_logic;
         io_data    : inout std_logic
       );
    '''

    def __init__(self):
        token_prefix_between_tokens.__init__(self, 'port', '011', lTokens, token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.prefixes = ['i_', 'o_', 'io_']
