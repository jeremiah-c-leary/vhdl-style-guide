# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import variable_declaration as token


class rule_100(Rule):
    """
    This rule checks for a single space before the identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable    size : integer;
       variable width : integer;

    **Fix**

    .. code-block:: vhdl

       variable size : integer;
       variable width : integer;
    """

    def __init__(self):
        Rule.__init__(self)
        self.disable = True
        self.left_token = token.variable_keyword
        self.right_token = token.identifier
