# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import file_declaration as token


class rule_100(Rule):
    """
    This rule checks for a single space before the identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       file           defaultImage : load_file_type open read_mode is load_file_name;

    **Fix**

    .. code-block:: vhdl

       file defaultImage : load_file_type open read_mode is load_file_name;
    """

    def __init__(self):
        Rule.__init__(self)
        self.disable = True
        self.left_token = token.file_keyword
        self.right_token = token.identifier
