
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.port_clause.close_parenthesis)


class rule_014(split_line_at_token):
    '''
    This rule checks the closing parenthesis of the port map is on a line by itself.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic);

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
        split_line_at_token.__init__(self, 'port', '014', lTokens)
        self.solution = 'Closing parenthesis must be on a line by itself.'
