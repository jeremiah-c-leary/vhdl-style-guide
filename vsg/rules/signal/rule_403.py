# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.assignment_operator, token.signal_declaration.semicolon])


class rule_403(Rule):
    """
    This rule checks the structure of multiline signal initializations that contain arrays.

    |configuring_array_multiline_structure_rules_link|

    .. NOTE:: The indenting of multiline array signal initializations is handled by the rule `signal_402 <signal_rules.html#signal-402>`_.

    **Violation**

    .. code-block:: vhdl

       signal rom : romq_type := (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       signal rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.assignment_operator = token.signal_declaration.assignment_operator
        self.semicolon = token.signal_declaration.semicolon
        self.phase = 5
