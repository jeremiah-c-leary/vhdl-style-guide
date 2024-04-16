# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.exponent.e_keyword)


class rule_500(token_case):
    """
    This rule checks the e keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

        12.5E-90
        6E57

    **Fix**

    .. code-block:: vhdl

        12.5e-90
        6e57
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
