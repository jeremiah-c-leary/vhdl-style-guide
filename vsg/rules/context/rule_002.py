# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import context_declaration as token


class rule_002(Rule):
    """
    This rule checks for a single space between the **context** keyword and the context identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       context   c1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    """

    def __init__(self):
        Rule.__init__(self)
        self.left_token = token.context_keyword
        self.right_token = token.identifier
