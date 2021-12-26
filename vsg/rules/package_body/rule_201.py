
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.is_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **package** keyword.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       package body FIFO_PKG is
         constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       package body FIFO_PKG is

         constant width : integer := 32;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'package_body', '201', lTokens)
