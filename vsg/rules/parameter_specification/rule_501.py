# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.parameter_specification.in_keyword)


class rule_501(token_case):
    """
    This rule checks the **in** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       for lv_thing IN t_thing loop

    **Fix**

    .. code-block:: vhdl

       for lv_thing in t_thing loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
