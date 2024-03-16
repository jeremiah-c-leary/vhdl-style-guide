# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.simple_variable_assignment.assignment, parser.todo])
lTokens.append([token.conditional_variable_assignment.assignment, parser.todo])
lTokens.append([token.selected_variable_assignment.assignment, parser.todo])


class rule_002(Rule):
    """
    This rule checks for a single space after the assignment.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

         counter :=0;
         count   :=     counter + 1;

    **Fix**

    .. code-block:: vhdl

         counter := 0;
         count   := counter + 1;
    """

    def __init__(self):
        super().__init__(lTokens)
