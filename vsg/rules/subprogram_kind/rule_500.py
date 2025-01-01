# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.subprogram_kind.procedure_keyword)


class rule_500(token_case):
    """
    This rule checks that the **procedure** keyword in subprogram kinds has the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end PROCEDURE parity;

       PROCEDURE my_proc is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       end procedure parity;

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
