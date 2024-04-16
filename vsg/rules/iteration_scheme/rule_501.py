# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.iteration_scheme.for_keyword)


class rule_501(Rule):
    """
    This rule checks the **for** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       FOR x in (31 downto 0) loop

    **Fix**

    .. code-block:: vhdl

       for x in (31 downto 0) loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
