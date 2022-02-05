
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import architecture_body as token


class rule_016(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines above the **begin** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         signal wr_en : std_logic;
       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         signal wr_en : std_logic;

       begin
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'architecture', '016', [token.begin_keyword])
