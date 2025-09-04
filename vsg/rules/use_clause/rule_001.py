# -*- coding: utf-8 -*-

from vsg.rules import does_token_value_match_none_of
from vsg.token import use_clause


class rule_001(does_token_value_match_none_of):
    """
    This rule checks for packages that have been restricted by the user.

    |configuring_library_and_package_name_restriction_rules_link|

    .. NOTE:: This rule is disabled by default.

    .. NOTE:: This rule is configured to restrict the std_logic_arith package by default.

    **Violation**

    .. code-block:: vhdl

       use ieee.std_logic_arith.all;
    """

    def __init__(self):
        super().__init__(use_clause.package_name)
        self.names = ["std_logic_arith"]

    def _get_solution(self, iLineNumber):
        return "Package name is on list of restricted names: " + ", ".join(self.names)
