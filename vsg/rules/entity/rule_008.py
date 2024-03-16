# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.entity_declaration.identifier)


class rule_008(token_case_with_prefix_suffix):
    """
    This rule checks the entity name has proper case in the entity declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       entity Fifo is

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
