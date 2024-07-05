# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.constant_keyword, token.constant_declaration.semicolon])


class rule_016(Rule):
    """
    This rule checks the structure of multiline constants that contain arrays.

    |configuring_array_multiline_structure_rules_link|

    .. NOTE:: The indenting of multiline array constants is handled by the rule `constant_012 <constant_rules.html#constant-012>`_.

    **Violation**

    .. code-block:: vhdl

       constant rom : romq_type := (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.assignment_operator = token.constant_declaration.assignment_operator
        self.semicolon = token.constant_declaration.semicolon
        self.phase = 5
