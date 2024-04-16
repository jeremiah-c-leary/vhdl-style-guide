# -*- coding: utf-8 -*-

from vsg.rules import blank_line_above_line_starting_with_token
from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.port_keyword)


class rule_001(blank_line_above_line_starting_with_token):
    """
    This rule checks for a blank line above the **port** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       entity FIFO is

         port (

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_blank_line"
