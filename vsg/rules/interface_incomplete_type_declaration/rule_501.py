# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.interface_incomplete_type_declaration.identifier)


class rule_501(token_case_with_prefix_suffix):
    """
    This rule checks the type name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic (
         type GENERIC_DATA_TYPE

    **Fix**

    .. code-block:: vhdl

       generic (
         type generic_data_type
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
