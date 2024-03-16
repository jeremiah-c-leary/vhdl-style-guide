# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.package_declaration.identifier)


class rule_010(token_case_with_prefix_suffix):
    """
    This rule checks the package name has proper case in the package declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package fifo_pkg is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
