

from vsg.rules import multiline_array_alignment as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.assignment_operator, token.constant_declaration.semicolon])


class rule_012(Rule):
    '''
    This rule checks the alignment of multiline constants that contain arrays.

    |configuring_multiline_indent_rules_link|

    .. NOTE:: The structure of multiline array constants is handled by the rule `constant_016 <constant_rules.html#constant-016>`_.

    **Violation**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
                0,
            65535,
            32768
         );

    **Fix**

    .. code-block:: vhdl

       constant rom : romq_type :=
       (
         0,
         65535,
         32768
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'constant', '012', lTokenPairs)
