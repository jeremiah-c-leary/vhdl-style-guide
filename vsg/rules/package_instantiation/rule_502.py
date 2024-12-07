# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.package_instantiation_declaration.is_keyword)


class rule_502(token_case_with_prefix_suffix):
    """
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package my_pkg IS new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
