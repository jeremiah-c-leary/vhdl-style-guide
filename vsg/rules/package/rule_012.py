
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.end_keyword)


class rule_012(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end package** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         constant depth : integer := 512;
       end package FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

         constant depth : integer := 512;

       end package FIFO_PKG;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'package', '012', lTokens)
