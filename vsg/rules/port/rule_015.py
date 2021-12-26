
from vsg import token

from vsg.rules import token_indent

lTokens = []
lTokens.append(token.port_clause.close_parenthesis)


class rule_015(token_indent):
    '''
    This rule checks the indent of the closing parenthesis for port maps.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
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
        token_indent.__init__(self, 'port', '015', lTokens)
