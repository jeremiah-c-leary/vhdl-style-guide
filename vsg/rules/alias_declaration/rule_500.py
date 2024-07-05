# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.alias_declaration.alias_keyword)


class rule_500(token_case):
    """
    This rule checks the **alias** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ALIAS alias_designator is name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
