# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.generic_clause.generic_keyword)


class rule_009(token_case):
    """
    This rule checks the **generic** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       GENERIC (

    **Fix**

    .. code-block:: vhdl

       generic (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
