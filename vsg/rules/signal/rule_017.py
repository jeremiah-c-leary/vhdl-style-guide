
from vsg.rules import multiline_constraint_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.signal_keyword, token.signal_declaration.semicolon])


class rule_017(Rule):
    '''
    This rule checks the structure of signal constraints.

    |configuring_multiline_constraint_rules_link|

    .. NOTE:: The indenting of multiline signal constraints is handled by the rule `jcl - fix this`_.

    **Violation**

    jcl - fix this

    .. code-block:: vhdl

       signal sig_a : my_type (0, 65535, 32768);

    **Fix**

    jcl - fix this

    .. code-block:: vhdl

       signal sig_a : romq_type (
         0,
         65535,
         32768
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'signal', '017')
        self.lTokenPairs = lTokenPairs
