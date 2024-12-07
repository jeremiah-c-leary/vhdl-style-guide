# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.package_body.package_simple_name)


class rule_502(token_case_with_prefix_suffix):
    """
    This rule checks the package name has proper case in the package body declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package body FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package body fifo_pkg is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
