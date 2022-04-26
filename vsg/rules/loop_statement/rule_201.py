
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import loop_statement as token


class rule_201(blank_line_below_line_ending_with_token):
    '''
    This rule checks for blank lines below the **loop** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       loop
         a <= b;

    **Fix**

    .. code-block:: vhdl

       loop

         a <= b;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'loop_statement', '201', [token.loop_keyword])
