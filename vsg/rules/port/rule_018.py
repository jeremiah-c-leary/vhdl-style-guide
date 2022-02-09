
from vsg.rules import token_case_n_token_after_tokens_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_018(token_case_n_token_after_tokens_between_tokens):
    '''
    This rule checks the port type has proper case if it is a VHDL keyword.

    |configuring_uppercase_and_lowercase_rules_link|


    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    STD_LOGIC;
         RD_EN    : in    std_logic;
         OVERFLOW : out   t_OVERFLOW;
         DATA     : inout STD_LOGIC_VECTOR(31 downto 0)
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   t_OVERFLOW;
         DATA     : inout std_logic_vector(31 downto 0)
       );
    '''

    def __init__(self):
        token_case_n_token_after_tokens_between_tokens.__init__(self, 'port', '018', 2, lTokens, oStart, oEnd, True)
        self.disabled = True
        self.groups.append('case::keyword')
