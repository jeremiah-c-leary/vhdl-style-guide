# -*- coding: utf-8 -*-

from vsg.rules import multiline_structure as Rule
from vsg.token import variable_declaration as token

lTokenPairs = []
lTokenPairs.append([token.assignment_operator, token.semicolon])


class rule_403(Rule):
    """
    This rule checks the structure of multiline variable initializations that contain arrays.

    |configuring_array_multiline_structure_rules_link|

    .. NOTE:: The indenting of multiline array variables is handled by the rule `variable_402 <variable_rules.html#variable-402>`_.

    **Violation**

    .. code-block:: vhdl

       variable rom : romq_type := (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       variable rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.assignment_operator = token.assignment_operator
        self.semicolon = token.semicolon
        self.phase = 5
