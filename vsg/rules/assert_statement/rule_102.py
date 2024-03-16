# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.assertion.severity_keyword)


class rule_102(Rule):
    """
    This rule checks for a single space after the **severity** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity       FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens)
