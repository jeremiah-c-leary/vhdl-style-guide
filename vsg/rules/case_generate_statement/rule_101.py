# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import case_generate_statement as token


class rule_101(Rule):
    """
    This rule checks for a single space before the **generate** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case data    generate

    **Fix**

    .. code-block:: vhdl

       case data generate
    """

    def __init__(self):
        Rule.__init__(self)
        self.left_token = parser.todo
        self.right_token = token.generate_keyword
