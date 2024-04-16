# -*- coding: utf-8 -*-

from vsg.rules import blank_line_below_line_ending_with_token as Rule
from vsg.token import entity_declaration as token


class rule_203(Rule):
    """
    This rule checks for blank lines below the semicolon in entity specifications.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end entity;
       library ieee;

    **Fix**

    .. code-block:: vhdl

       end entity;

       library ieee;
    """

    def __init__(self):
        super().__init__([token.semicolon])
