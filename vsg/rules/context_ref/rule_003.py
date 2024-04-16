# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_003(token_case):
    """
    This rule checks the **context** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       CONTEXT c1;

    **Fix**

    .. code-block:: vhdl

       context c1;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
