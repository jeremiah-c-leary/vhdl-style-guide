# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.null_statement.null_keyword)


class rule_500(Rule):
    """
    This rule checks the **null** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       NULL;

    **Fix**

    .. code-block:: vhdl

       null;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
