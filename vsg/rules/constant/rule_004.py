# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.constant_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    """
    This rule checks the constant identifier has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant SIZE : integer := 1;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
