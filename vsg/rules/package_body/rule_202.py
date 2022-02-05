
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_body.end_keyword)


class rule_202(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         constant depth : integer := 512;
       end package body FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

         constant depth : integer := 512;

       end package body FIFO_PKG;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'package_body', '202', lTokens)
