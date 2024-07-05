# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_alignment_between_tokens

lTokenPairs = []
lTokenPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])


class rule_020(multiline_alignment_between_tokens):
    """
    This rule checks the indentation of multiline sensitivity lists.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                            rd_full, wr_full,
                   overflow, underflow
                        ) is begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full,
                         overflow, underflow
                        ) is
       begin
    """

    def __init__(self):
        super().__init__(lTokenPairs, True)
