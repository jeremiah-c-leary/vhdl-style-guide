# -*- coding: utf-8 -*-

from vsg.rules import does_token_value_match_none_of
from vsg.token import logical_name_list


class rule_012(does_token_value_match_none_of):
    """
    This rule checks for libraries that have been restricted by the user.

    |configuring_library_and_package_name_restriction_rules_link|

    .. NOTE:: This rule is disabled by default.

    **Violation**

    .. code-block:: vhdl

       library bad_lib;
    """

    def __init__(self):
        super().__init__(logical_name_list.logical_name)

    def _get_solution(self, iLineNumber):
        return "Library name is on list of restricted names: " + ", ".join(self.names)
