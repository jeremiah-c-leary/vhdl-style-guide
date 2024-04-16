# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    """
    This rule checks the variable name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable COUNT : integer;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
