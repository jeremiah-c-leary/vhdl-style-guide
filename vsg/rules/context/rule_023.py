
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_023(blank_line_below_line_ending_with_token):
    '''
    This rule adds a blank line below the **is** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       context c1 is
         library IEEE;

    **Fix**

    .. code-block:: vhdl

       context c1 is

         library IEEE;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'context', '023', [token.is_keyword])
