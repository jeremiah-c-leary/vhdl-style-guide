# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import existence_of_tokens_which_should_not_occur

lTokens = []
lTokens.append(token.variable_declaration.assignment_operator)


class rule_007(existence_of_tokens_which_should_not_occur):
    """
    This rule checks for default assignments in variable declarations.

    **Violation**

    .. code-block:: vhdl

       variable count : integer := 32;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Remove default assignment."
