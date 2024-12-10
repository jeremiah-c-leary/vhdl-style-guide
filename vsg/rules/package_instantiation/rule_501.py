# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens_with_prefix_suffix

lTokens = []
lTokens.append(token.identifier.identifier)

oStart = token.package_instantiation_declaration.package_keyword
oEnd = token.package_instantiation_declaration.is_keyword


class rule_501(token_case_in_range_bounded_by_tokens_with_prefix_suffix):
    """
    This rule checks the instantiated package name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package MY_PKG is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.groups.append("case::name")
