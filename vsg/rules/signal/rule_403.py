# -*- coding: utf-8 -*-

from vsg.token import signal_declaration as token
from vsg.rules import multiline_structure as Rule

lTokenPairs = []
lTokenPairs.append([token.assignment_operator, token.semicolon])


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
        self.assignment_operator = token.assignment_operator
        self.semicolon = token.semicolon
        self.phase = 5
