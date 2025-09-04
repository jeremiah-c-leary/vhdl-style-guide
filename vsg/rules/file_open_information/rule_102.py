# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import file_open_information as token


class rule_102(Rule):
    """
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       file defaultImage : load_file_type open read_mode     is load_file_name;

    **Fix**

    .. code-block:: vhdl

       file defaultImage : load_file_type open read_mode is load_file_name;
    """

    def __init__(self):
        Rule.__init__(self)
        self.left_token = token.file_open_kind_expression
        self.right_token = token.is_keyword
