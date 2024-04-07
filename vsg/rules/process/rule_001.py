# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.postponed_keyword)
lTokens.append(token.process_statement.process_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of the process declaration.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

       begin

       proc_a : process (rd_en, wr_en, data_in, data_out,

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

       begin

         proc_a : process (rd_en, wr_en, data_in, data_out,
    """

    def __init__(self):
        super().__init__(lTokens)
