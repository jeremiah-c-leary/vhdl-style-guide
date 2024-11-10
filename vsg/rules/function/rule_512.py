# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.function_specification.impure_keyword)


class rule_512(Rule):
    """
    This rule checks the **impure** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       IMPURE function overflow (a: integer) return integer is

    **Fix**

    .. code-block:: vhdl

       impure function overflow (a: integer) return integer is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
