# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.package_body.is_keyword)


class rule_503(token_case):
    """
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package body fifo_pkg IS

    **Fix**

    .. code-block:: vhdl

       package body fifo_pkg is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
