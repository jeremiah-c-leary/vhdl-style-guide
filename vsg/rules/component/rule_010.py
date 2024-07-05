# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_010(token_case):
    """
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END component fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
