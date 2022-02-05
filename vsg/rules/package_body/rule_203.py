
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.semicolon)


class rule_203(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **end package** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end package body FIFO_PKG;
       library ieee;

    **Fix**

    .. code-block:: vhdl

       end package body FIFO_PKG;

       library ieee;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'package_body', '203', lTokens)
