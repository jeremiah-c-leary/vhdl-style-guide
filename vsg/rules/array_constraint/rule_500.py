# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.array_constraint.open_keyword)


class rule_500(token_case):
    """
    This rule checks the **open** keyword in array constraints has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype t_my_array is t_array(OPEN)(t_range);


    **Fix**

    .. code-block:: vhdl

       subtype t_my_array is t_array(open)(t_range);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
