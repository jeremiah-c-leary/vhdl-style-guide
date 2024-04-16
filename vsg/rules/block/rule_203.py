# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_203(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **begin** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       begin
         a <= b;

    **Fix**

    .. code-block:: vhdl

       begin

         a <= b;
    """

    def __init__(self):
        super().__init__(lTokens)
