# -*- coding: utf-8 -*-

from vsg.rules import file_length


class rule_002(file_length):
    """
    This rule checks the length of a file.

    |configuring_length_rules_link|
    """

    def __init__(self):
        super().__init__()
