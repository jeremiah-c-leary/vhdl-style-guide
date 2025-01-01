# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.subprogram_instantiation_declaration.uninstantiated_subprogram_name)


class rule_503(token_case_with_prefix_suffix):
    """
    This rule checks the uninstantiated subprogram name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure my_proc is new MY_GENERIC_PROC

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
