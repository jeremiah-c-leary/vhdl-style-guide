# -*- coding: utf-8 -*-

from vsg.rules import token_does_not_exist_before_token as Rule
from vsg.token import process_statement as token

oFirstToken = token.process_label

oSecondToken = token.process_keyword


class rule_016(Rule):
    """
    This rule checks the process has a label.

    **Violation**

    .. code-block:: vhdl

       process (rd_en, wr_en, data_in, data_out,
                rd_full, wr_full
               ) is
       begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    """

    def __init__(self):
        super().__init__(oFirstToken, oSecondToken)
        self.solution = "Add label for process statement"
        self.fixable = False
