# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.package_declaration.package_keyword)


class rule_003(previous_line):
    """
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
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_code"
