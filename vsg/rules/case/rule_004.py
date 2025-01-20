# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_004(Rule):
    """
    This rule checks for a single space after the **when** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      case data is

        when   3 =>

    **Fix**

    .. code-block:: vhdl

      case data is

        when 3 =>
    """

    def __init__(self):
        Rule.__init__(self, lTokens)
