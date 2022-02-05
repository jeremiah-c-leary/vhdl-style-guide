
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import architecture_body as token


class rule_015(blank_line_below_line_ending_with_token):
    '''
    This rule checks for blank lines below the architecture declaration.

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
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '015', [token.is_keyword])
