# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.use_clause.library_name)


class rule_500(Rule):
    """
    This rule checks the library name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use IEEE.std_logic_1164.all;

       use my_LIB.all;

    **Fix**

    .. code-block:: vhdl

       use ieee.std_logic_1164.all;

       use my_lib.all;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
        self.configuration.append("case_exceptions")
