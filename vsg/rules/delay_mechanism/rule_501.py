# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.delay_mechanism.inertial_keyword)


class rule_501(token_case):
    """
    This rule checks the *inertial* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= INERTIAL 1 after 10 ns;

    **Fix**

    .. code-block:: vhdl

       a <= inertial 1 after 10 ns;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
