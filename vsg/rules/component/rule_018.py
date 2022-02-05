
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import component_declaration as token


class rule_018(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **end component** line.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end component fifo;
       signal rd_en : std_logic;


    **Fix**

    .. code-block:: vhdl

       end component fifo;

       signal rd_en : std_logic;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'component', '018', [token.semicolon])
