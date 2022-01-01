
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import architecture_body as token


class rule_017(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **begin** keyword.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       begin
         wr_en <= '0';

    **Fix**

    .. code-block:: vhdl

       begin

         wr_en <= '0';
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '017', [token.begin_keyword])
