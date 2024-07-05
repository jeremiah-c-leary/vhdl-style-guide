# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.attribute_declaration.attribute_keyword)


class rule_500(token_case):
    """
    This rule checks the **attribute** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ATTRIBUTE max_delay : time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
