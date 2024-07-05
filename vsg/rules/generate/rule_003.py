# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.case_generate_statement.semicolon)
lTokens.append(token.for_generate_statement.semicolon)
lTokens.append(token.if_generate_statement.semicolon)


class rule_003(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **end generate** keywords.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end generate ram_array;
       wr_en <= '1';

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;

       wr_en <= '1';
    """

    def __init__(self):
        super().__init__(lTokens)
