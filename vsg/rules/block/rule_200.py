# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_200(previous_line):
    """
    This rule checks for blank lines or comments above the block label.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= b;
       block_label : block is

    **Fix**

    .. code-block:: vhdl

       a <= b;

       block_label : block is
    """

    def __init__(self):
        super().__init__(lTokens)
