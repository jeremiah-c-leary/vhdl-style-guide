# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import remove_lines_starting_with_token_between_token_pairs

lTokens = []
lTokens.append([token.simple_variable_assignment.simple_name, token.simple_variable_assignment.semicolon])

oRemoveToken = parser.comment


class rule_006(remove_lines_starting_with_token_between_token_pairs):
    """
    This rule checks for comments in multiline variable assignments.

    **Violation**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
                    -- Add in more stuff
                    30 + 35;

    **Fix**

    .. code-block:: vhdl

         counter := 1 + 4 + 10 + 25 +
                    30 + 35;
    """

    def __init__(self):
        super().__init__(oRemoveToken, lTokens)
        self.solution = "Remove comments inside variable assignment"
        self.fixable = False
