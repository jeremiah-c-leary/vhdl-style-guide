# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_022(blank_line_below_line_ending_with_token):
    """
    This rule checks for a blank line below the **begin** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
         rd_en <= '0';

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin

         rd_en <= '0';
    """

    def __init__(self):
        super().__init__(lTokens)
