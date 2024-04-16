# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.assertion.keyword)


class rule_500(token_case):
    """
    This rule checks the **assert** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ASSERT WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
