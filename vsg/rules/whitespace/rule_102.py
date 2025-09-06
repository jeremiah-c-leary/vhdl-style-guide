# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.direction.downto)
lTokens.append(token.direction.to)


class rule_102(Rule):
    """
    This rule checks for a single space before direction keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      x <= y(7     downto 0);
      x <= y(0     to 7);

    **Fix**

    .. code-block:: vhdl

      x <= y(7 downto 0);
      x <= y(0 to 7);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = 1
