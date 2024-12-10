# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.generic_map_aspect.generic_keyword)
lTokens.append(token.generic_map_aspect.map_keyword)


class rule_001(token_case):
    """
    This rule checks the **generic map** keywords have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       GENERIC MAP (

    **Fix**

    .. code-block:: vhdl

       generic map (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
