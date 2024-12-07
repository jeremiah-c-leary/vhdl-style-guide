# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.package_instantiation_declaration.package_keyword)


class rule_500(token_case):
    """
    This rule checks the package keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PACKAGE my_pkg is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
