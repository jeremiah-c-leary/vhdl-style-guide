# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import constant_declaration as token


class rule_101(Rule):
    """
    This rule checks for a single space before the identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant    size : integer := 1;
       constant width : integer := 32;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
       constant width : integer := 32;
    """

    def __init__(self):
        Rule.__init__(self)
        self.disable = True
        self.left_token = token.constant_keyword
        self.right_token = token.identifier
