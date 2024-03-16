# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.process_statement.semicolon)


class rule_011(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **end process** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end process proc_a;
       wr_en <= wr_en;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;

       wr_en <= wr_en;
    """

    def __init__(self):
        super().__init__(lTokens)
