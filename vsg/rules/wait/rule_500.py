# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.wait_statement.wait_keyword)


class rule_500(Rule):
    """
    This rule checks the **wait** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       WAIT for 100 ns;

    **Fix**

    .. code-block:: vhdl

       wait for 100 ns;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
