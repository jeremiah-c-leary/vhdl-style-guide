# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_005(token_case):
    """
    This rule checks the **use** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       library ieee;
         USE ieee.std_logic_1164.all;
         Use ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
