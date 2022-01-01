
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.semicolon)


class rule_205(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the semicolon.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       end block block_label;
       a <= b;

    **Fix**

    .. code-block:: vhdl

       end block block_label;

       a <= b;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'block', '205', lTokens)
