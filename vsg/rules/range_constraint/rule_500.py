# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.range_constraint.range_keyword)


class rule_500(token_case):
    """
    This rule checks the **range** keyword in range constraints has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype t_range is natural RANGE 1 to 0;

    **Fix**

    .. code-block:: vhdl

       subtype t_range is natural range 1 to 0;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
