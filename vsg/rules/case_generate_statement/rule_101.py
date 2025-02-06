# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.case_generate_statement.generate_keyword)


class rule_101(Rule):
    """
    This rule checks for a single space before the **generate** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case data    generate

    **Fix**

    .. code-block:: vhdl

       case data generate
    """

    def __init__(self):
        Rule.__init__(self, lTokens)
