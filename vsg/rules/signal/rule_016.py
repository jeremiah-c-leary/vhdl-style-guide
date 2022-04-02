
from vsg.rules import multiline_declaration_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.signal_keyword, token.signal_declaration.semicolon])


class rule_016(Rule):
    '''
    This rule checks the structure of multiline signal declarations.

    |configuring_multiline_structure_rules_link|

    .. NOTE:: The indenting of multiline array constants is handled by the rule `constant_012 <constant_rules.html#constant-012>`_.

    **Violation**

    .. code-block:: vhdl

       signal sig_a : my_type (0, 65535, 32768);

    **Fix**

    .. code-block:: vhdl

       signal sig_a : romq_type (
         0,
         65535,
         32768
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'signal', '016', lTokenPairs)
