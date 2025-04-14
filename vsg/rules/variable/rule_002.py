# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.variable_declaration.shared_keyword)
lTokens.append(token.variable_declaration.variable_keyword)


class rule_002(token_case):
    """
    This rule checks that the keywords **shared** and **variable** have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       VARIABLE count : integer;

       SHARED VARIABLE size : integer;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;

       shared variable size : integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
