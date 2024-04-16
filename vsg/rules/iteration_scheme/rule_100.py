# -*- coding: utf-8 -*-

from vsg.rules.whitespace_after_token import Rule
from vsg.token import iteration_scheme as token

lTokens = []
lTokens.append(token.while_keyword)


class rule_100(Rule):
    """
    This rule checks that a single space exists after the **while** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       while(condition)

       while      (condition)

    **Fix**

    .. code-block:: vhdl

       while (condition)

       while (condition)
    """

    def __init__(self):
        super().__init__(lTokens)
