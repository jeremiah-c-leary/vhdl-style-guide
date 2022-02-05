
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import architecture_body as token


class rule_018(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end architecture** declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         rd_en <= '1';
       end architecture RTL;

    **Fix**

    .. code-block:: vhdl

         rd_en <= '1';

       end architecture RTL;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'architecture', '018', [token.end_keyword])
