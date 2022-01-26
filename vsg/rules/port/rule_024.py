
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.close_parenthesis)

class rule_024(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    This rule checks for blank lines before the close parenthesis in port declarations.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : std_logic;
         RD_EN    : std_logic;
         OVERFLOW : std_logic;
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
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'port', '024', lTokens, iAllow=0)
        self.solution = 'Remove blank lines above ).'
