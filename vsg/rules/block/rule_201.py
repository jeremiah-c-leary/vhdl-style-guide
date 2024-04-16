# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_several_possible_tokens

lTokens = []
lTokens.append(token.block_statement.block_keyword)
lTokens.append(token.block_statement.guard_close_parenthesis)
lTokens.append(token.block_statement.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.block_statement.begin_keyword)


class rule_201(blank_line_below_line_ending_with_several_possible_tokens):
    """
    This rule checks for a blank line below the **block** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       block_label : block is
         constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       block_label : block is

         constant width : integer := 32;
    """

    def __init__(self):
        super().__init__(lTokens, lAllowTokens)
