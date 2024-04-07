# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.label_name)
lTokens.append(token.procedure_call_statement.label)


class rule_500(token_case):
    """
    This rule checks the label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PROCEDURE_CALL_LABEL : WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       procedure_call_label : WR_EN(parameter);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::label")
