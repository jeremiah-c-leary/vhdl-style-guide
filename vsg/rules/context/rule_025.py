
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_025(blank_line_below_line_ending_with_token):
    '''
    This rule adds a blank line below the context semicolon.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       end context;
       entity fifo is

    **Fix**

    .. code-block:: vhdl

       end context;

       entity fifo is
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'context', '025', [token.semicolon])
