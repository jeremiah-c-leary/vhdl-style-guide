# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.subprogram_instantiation_declaration.identifier)


class rule_500(token_case_with_prefix_suffix):
    """
    This rule checks the instantiated package name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure MY_PROC is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
