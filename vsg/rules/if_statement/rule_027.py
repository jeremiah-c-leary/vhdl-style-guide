# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.if_statement.else_keyword)


class rule_027(token_case):
    """
    This rule checks the **else** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ELSE

    **Fix**

    .. code-block:: vhdl

       else
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
