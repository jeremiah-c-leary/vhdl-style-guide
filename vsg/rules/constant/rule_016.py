
from vsg.rules import multiline_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.constant_keyword, token.constant_declaration.semicolon])


class rule_016(Rule):
    '''
    This rule checks the structure of multiline constants that contain arrays.

    |configuring_multiline_structure_rules_link|

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
    '''

    def __init__(self):
        Rule.__init__(self, 'constant', '016', lTokenPairs)
