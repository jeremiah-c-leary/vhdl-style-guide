# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_016(token_case):
    """
    This rule checks the **when** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         WHEN a =>
         When b =>
         when c =>

    **Fix**

    .. code-block:: vhdl

         when a =>
         when b =>
         when c =>
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
