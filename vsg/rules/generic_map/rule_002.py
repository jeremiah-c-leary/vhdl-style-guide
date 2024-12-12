# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    token_case_formal_part_of_association_element_in_map_between_tokens,
)

oStart = token.generic_map_aspect.generic_keyword
oEnd = token.generic_map_aspect.close_parenthesis

sMapType = "generic"


class rule_002(token_case_formal_part_of_association_element_in_map_between_tokens):
    """
    This rule checks generic names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         generic map (
           DEPTH => 512,
           WIDTH => 32
         )

    **Fix**

    .. code-block:: vhdl

         generic map (
           depth => 512,
           width => 32
         )
    """

    def __init__(self):
        super().__init__(sMapType, oStart, oEnd)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.groups.append("case::name")
