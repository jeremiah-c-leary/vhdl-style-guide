# -*- coding: utf-8 -*-

from vsg.rules.blank_line_above_line_starting_with_token_when_between_tokens import Rule
from vsg.token import entity_declaration as between, generic_clause as token

lTokens = []
lTokens.append(token.generic_keyword)


class rule_200(Rule):
    """
    This rule checks for blank lines above the **generic** keyword in entity specifications.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       entity fifo is



         generic (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         generic (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_blank_line"
        self.lBetweenTokenPairs = [between.entity_keyword, between.semicolon]
