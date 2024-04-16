# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.package_body.end_body_keyword)


class rule_506(token_case):
    """
    This rule checks the **body** keyword in the **end package body** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end package BODY fifo_pkg;

    **Fix**

    .. code-block:: vhdl

       end package body fifo_pkg;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
