# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.loop_statement.loop_keyword)


class rule_500(Rule):
    """
    This rule checks the **loop** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       while (condition) LOOP

    **Fix**

    .. code-block:: vhdl

       while (condition) loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
