# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import number_of_lines_between_tokens

oLeftToken = token.process_statement.process_keyword
oRightToken = token.process_statement.semicolon

iLines = 500


class rule_003(number_of_lines_between_tokens):
    """
    This rule checks the length of a process statement.

    |configuring_length_rules_link|
    """

    def __init__(self):
        super().__init__(oLeftToken, oRightToken, iLines)
