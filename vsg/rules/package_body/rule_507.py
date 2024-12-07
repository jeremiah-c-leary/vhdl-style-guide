# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.package_body.end_package_simple_name)


class rule_507(token_case_with_prefix_suffix):
    """
    This rule checks the package name has proper case on the end package body declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end package body FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package body fifo_pkg;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
