# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.package_declaration.is_keyword)


class rule_011(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **package** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       package FIFO_PKG is
         constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       package FIFO_PKG is

         constant width : integer := 32;
    """

    def __init__(self):
        super().__init__(lTokens)
