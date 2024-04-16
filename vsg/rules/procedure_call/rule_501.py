# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.postponed_keyword)


class rule_501(token_case):
    """
    This rule checks the **postponed** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       POSTPONED WR_EN(parameter)

    **Fix**

    .. code-block:: vhdl

       postponed WR_EN(parameter)
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
