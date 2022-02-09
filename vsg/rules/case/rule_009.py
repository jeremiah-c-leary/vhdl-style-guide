
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import case_statement as token


class rule_009(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         when others =>
           null;
       end case;

    **Fix**

    .. code-block:: vhdl

         when others =>
           null;

       end case;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'case', '009', [token.end_keyword])
