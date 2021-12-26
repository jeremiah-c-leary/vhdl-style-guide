
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.semicolon)


class rule_205(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the semicolon at the end of the procedure declaration.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       end procedure average_samples;
       signal wr_en : std_logic;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;

       signal wr_en : std_logic;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'procedure', '205', lTokens)
