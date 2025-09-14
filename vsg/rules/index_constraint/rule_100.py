# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.index_constraint.open_parenthesis)


class rule_100(Rule):
    """
    This rule checks for whitespace before the opening parenthesis.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      subtype my_array3 is my_array2(open)         (7 downto 0);

    **Fix**

    .. code-block:: vhdl

      subtype my_array3 is my_array2(open)(7 downto 0);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 0
