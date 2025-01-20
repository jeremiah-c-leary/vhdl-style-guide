# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.case_statement.case_keyword)


class rule_002(Rule):
    """
    This rule checks for a single space after the **case** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case    data is


    **Fix**

    .. code-block:: vhdl

       case data is
    """

    def __init__(self):
        Rule.__init__(self, lTokens)
