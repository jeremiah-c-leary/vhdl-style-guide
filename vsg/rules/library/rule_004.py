# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_004(token_case):
    """
    This rule checks the **library** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       Library ieee;

       LIBRARY fifo_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;

       library fifo_dsn;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
