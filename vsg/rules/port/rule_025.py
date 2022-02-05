
from vsg.rules import token_suffix_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)


class rule_025(token_suffix_between_tokens):
    '''
    This rule checks for valid suffixes on port identifiers.
    The default port suffixes are *_i*, *_o*, *_io*.

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
         wr_en_i    : in    std_logic;
         rd_en_i    : in    std_logic;
         overflow_o : out   std_logic;
         data_io    : inout std_logic
       );
    '''

    def __init__(self):
        token_suffix_between_tokens.__init__(self, 'port', '025', lTokens, token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.suffixes = ['_i', '_o', '_io']
