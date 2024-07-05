# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import subtype_declaration as token


class rule_100(Rule):
    """
    This rule checks for a single space before the identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype         my_subtype is range 0 to 9;

    **Fix**

    .. code-block:: vhdl

       subtype my_subtype is range 0 to 9;
    """

    def __init__(self):
        Rule.__init__(self)
        self.disable = True
        self.left_token = token.subtype_keyword
        self.right_token = token.identifier
