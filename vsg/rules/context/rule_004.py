# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.context_declaration.context_keyword)


class rule_004(token_case):
    """
    This rule checks the **context** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       CONTEXT c1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
