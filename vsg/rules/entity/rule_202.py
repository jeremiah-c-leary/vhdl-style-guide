# -*- coding: utf-8 -*-

from vsg.rules.blank_line_above_line_starting_with_token_when_between_tokens import Rule
from vsg.token import entity_declaration as between, port_clause as token

lTokens = []
lTokens.append(token.port_keyword)


class rule_202(Rule):
    """
    This rule checks for blank lines above the **port** keyword in entity specifications.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       entity fifo is



         port (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         port (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_blank_line"
        self.lBetweenTokenPairs = [between.entity_keyword, between.semicolon]
