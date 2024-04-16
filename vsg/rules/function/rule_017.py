# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.function_specification.designator)


class rule_017(token_case):
    """
    This rule checks the function designator has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       function OVERflow (a: integer) return integer is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
        self.configuration.append("case_exceptions")
