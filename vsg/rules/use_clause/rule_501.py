# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.use_clause.package_name)


class rule_501(Rule):
    """
    This rule checks the package name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use ieee.STD_LOGIC_1164.all;

    **Fix**

    .. code-block:: vhdl

       use ieee.std_logic_1164.all;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
        self.configuration.append("case_exceptions")
