
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_003(previous_line):
    '''
    This rule checks for blank lines or comments above the **package** keyword.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       package FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package FIFO_PKG is
    '''

    def __init__(self):
        previous_line.__init__(self, 'package', '003', lTokens)
        self.style = 'no_code'
