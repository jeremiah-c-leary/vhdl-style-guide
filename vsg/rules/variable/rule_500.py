# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.variable_declaration.shared_keyword)


class rule_500(token_case):
    """
    This rule checks that the keyword **shared** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       SHARED variable size : integer;

    **Fix**

    .. code-block:: vhdl

       shared variable size : integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
