# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.sensitivity_clause.on_keyword)


class rule_501(Rule):
    """
    This rule checks the **on** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       wait ON condition;

    **Fix**

    .. code-block:: vhdl

       wait on condition;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
