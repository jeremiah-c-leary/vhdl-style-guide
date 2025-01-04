# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.parameter_specification.identifier)


class rule_500(Rule):
    """
    This rule checks the parameter identifier has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       for LV_THING in t_thing loop

    **Fix**

    .. code-block:: vhdl

       for lv_thing in t_thing loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
