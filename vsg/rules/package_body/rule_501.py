# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.package_body.body_keyword)


class rule_501(token_case):
    """
    This rule checks the **body** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       package BODY FIFO_PKG is

    **Fix**

    .. code-block:: vhdl

       package body FIFO_PKG is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
