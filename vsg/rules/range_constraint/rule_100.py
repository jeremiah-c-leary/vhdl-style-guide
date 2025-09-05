# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.range_constraint.range_keyword)


class rule_100(Rule):
    """
    This rule checks for a single space before the **range** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      subtype my_range is natural     range 0 to 7;

    **Fix**

    .. code-block:: vhdl

      subtype my_range is natural range 0 to 7;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 1
