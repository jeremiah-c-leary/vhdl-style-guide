
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement as token


class rule_010(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **end case** keywords.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       end case;
       a <= '1';

    **Fix**

    .. code-block:: vhdl

       end case;

       a <= '1';
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '010', [token.semicolon])
