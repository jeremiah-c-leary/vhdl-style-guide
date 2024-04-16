# -*- coding: utf-8 -*-

from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace
from vsg.token import procedure_call_statement as token


class rule_001(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    """
    This rule checks for labels on procedure call statements.
    Labels on procedure calls are optional and do not provide additional information.

    **Violation**

    .. code-block:: vhdl

       WR_EN_OUTPUT : WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       WR_EN(parameter);
    """

    def __init__(self):
        super().__init__(token.label, token.label_colon)
        self.solution = "Remove Label"
