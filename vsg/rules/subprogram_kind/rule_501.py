# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.subprogram_kind.function_keyword)


class rule_501(token_case):
    """
    This rule checks that the **function** keyword in subprogram kinds has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end FUNCTION parity;

       FUNCTION my_func is new my_generic_func

    **Fix**

    .. code-block:: vhdl

       end function parity;

       function my_func is new my_generic_func
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
