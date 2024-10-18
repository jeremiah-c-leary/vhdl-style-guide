# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.next_statement.when_keyword)


class rule_501(Rule):
    """
    This rule checks the **when** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       next WHEN condition;

    **Fix**

    .. code-block:: vhdl

       next when condition;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")