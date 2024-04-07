# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.entity_declaration.end_entity_keyword)


class rule_014(token_case):
    """
    This rule checks the **entity** keyword has proper case in the closing of the entity declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end ENTITY fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
