# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.function_specification.pure_keyword)


class rule_509(Rule):
    """
    This rule checks the **pure** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PURE function overflow (a: integer) return integer is

    **Fix**

    .. code-block:: vhdl

       pure function overflow (a: integer) return integer is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
