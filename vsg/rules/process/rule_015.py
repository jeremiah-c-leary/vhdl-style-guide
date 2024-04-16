# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.process_statement.process_keyword)
lTokens.append(token.process_statement.process_label)


class rule_015(previous_line):
    """
    This rule checks for blank lines or comments above the **process** declaration.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       -- This process performs FIFO operations.
       proc_a : process (rd_en, wr_en, data_in, data_out,

       wr_en <= wr_en;
       proc_a : process (rd_en, wr_en, data_in, data_out,

    **Fix**

    .. code-block:: vhdl

       -- This process performs FIFO operations.
       proc_a : process (rd_en, wr_en, data_in, data_out,

       wr_en <= wr_en;

       proc_a : process (rd_en, wr_en, data_in, data_out,
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_code"
