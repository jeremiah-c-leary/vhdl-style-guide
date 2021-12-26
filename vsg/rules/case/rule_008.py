
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement as token


class rule_008(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **is** keyword.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       case data is
         when 0 =>

    **Fix**

    .. code-block:: vhdl

       case data is

         when 0 =>
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '008', [token.is_keyword])
