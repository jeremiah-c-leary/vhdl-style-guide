
from vsg import token

from vsg.rules import whitespace_before_tokens_in_between_tokens

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_file_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_020(whitespace_before_tokens_in_between_tokens):
    '''
    This rule checks for at least one space before the colon.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW: out   std_logic;
         DATA     : inout std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
       );
    '''
    def __init__(self):
        whitespace_before_tokens_in_between_tokens.__init__(self, 'port', '020', lTokens, oStart, oEnd)
        self.solution = 'Add a space before the :.'
