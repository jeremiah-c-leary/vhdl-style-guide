
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_204(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end** keyword.

    Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

    **Violation**

    .. code-block:: vhdl

       begin

         a <= b;
       end block block_label;

    **Fix**

    .. code-block:: vhdl

       begin

         a <= b;

       end block block_label;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'block', '204', lTokens)
