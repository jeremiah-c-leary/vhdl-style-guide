# -*- coding: utf-8 -*-


from vsg.rules import multiline_array_alignment as Rule
from vsg.token import variable_declaration as token

lTokenPairs = []
lTokenPairs.append([token.assignment_operator, token.semicolon])


class rule_402(Rule):
    """
    This rule checks the alignment of multiline variables that contain arrays.

    |configuring_multiline_indent_rules_link|

    .. NOTE:: The structure of multiline array variables is handled by the rule `variable_403 <variable_rules.html#variable-403>`_.

    **Violation**

    .. code-block:: vhdl

       variable rom : romq_type :=
       (
                0,
            65535,
            32768
         );

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
