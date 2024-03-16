# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import alias_declaration as token


class rule_103(Rule):
    """
    This rule checks for a single space before the designator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       alias          alias_designator is name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    """

    def __init__(self):
        Rule.__init__(self)
        self.disable = True
        self.left_token = token.alias_keyword
        self.right_token = token.alias_designator
