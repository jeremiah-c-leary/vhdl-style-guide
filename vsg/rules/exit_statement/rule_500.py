# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.exit_statement.exit_keyword)


class rule_500(Rule):
    """
    This rule checks the **exit** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       EXIT when condition;

    **Fix**

    .. code-block:: vhdl

       exit when condition;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
