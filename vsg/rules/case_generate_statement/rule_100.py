# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import case_generate_statement as token


class rule_100(Rule):
    """
    This rule checks for a single space after the **case** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case    data generate


    **Fix**

    .. code-block:: vhdl

       case data generate
    """

    def __init__(self):
        Rule.__init__(self)
        self.left_token = token.case_keyword
        self.right_token = parser.todo
