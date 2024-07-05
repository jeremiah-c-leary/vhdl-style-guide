# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_above_line_starting_with_token

lTokens = []
lTokens.append(token.package_body.end_keyword)


class rule_202(blank_line_above_line_starting_with_token):
    """
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
    """

    def __init__(self):
        super().__init__(lTokens)
