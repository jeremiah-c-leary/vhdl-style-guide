
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_203(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **begin** keyword.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       begin
         a <= b;

    **Fix**

    .. code-block:: vhdl

       begin

         a <= b;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'block', '203', lTokens)
