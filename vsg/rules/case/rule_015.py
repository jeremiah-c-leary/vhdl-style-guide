# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.case_statement.is_keyword)


class rule_015(token_case):
    """
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         case address IS

         case address Is

         case address iS

    **Fix**

    .. code-block:: vhdl

         case address is

         case address is

         case address is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
