
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.architecture_body.semicolon)


class rule_200(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the end architecture statement.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       end architecture;
       library ieee;

    **Fix**

    .. code-block:: vhdl

       end architecture;

       library ieee;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'architecture', '200', lTokens)
