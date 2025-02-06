# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.case_statement.is_keyword)


class rule_003(Rule):
    """
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case data    is

    **Fix**

    .. code-block:: vhdl

       case data is
    """

    def __init__(self):
        Rule.__init__(self, lTokens)
