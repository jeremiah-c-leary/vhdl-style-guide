# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.use_clause.all_keyword)


class rule_503(token_case):
    """
    This rule checks the **all** keyword called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use ieee.std_logic_1164.ALL;

    **Fix**

    .. code-block:: vhdl

       use ieee.std_logic_1164.all;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
