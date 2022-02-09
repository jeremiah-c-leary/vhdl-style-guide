
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.package_body.package_keyword)


class rule_200(previous_line):
    '''
    This rule checks for blank lines or comments above the **package** keyword.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       library ieee;
       package body FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package body FIFO_PKG is
    '''

    def __init__(self):
        previous_line.__init__(self, 'package_body', '200', lTokens)
