# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.function_specification.return_keyword)


class rule_501(Rule):
    """
    This rule checks the **return** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) RETURN integer is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
