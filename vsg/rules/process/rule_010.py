# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_010(split_line_at_token):
    """
    This rule checks the **begin** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Closing parenthesis must be on a line by itself."
