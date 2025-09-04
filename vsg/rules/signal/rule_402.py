# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules import multiline_array_alignment as Rule

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.assignment_operator, token.signal_declaration.semicolon])


class rule_402(Rule):
    """
    This rule checks the alignment of multiline signal initializations that contain arrays.

    |configuring_multiline_indent_rules_link|

    .. NOTE:: The structure of multiline array signal initializations is handled by the rule `signal_403 <signal_rules.html#signal-403>`_.

    **Violation**

    .. code-block:: vhdl

       signal rom : romq_type :=
       (
                0,
            65535,
            32768
         );

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
