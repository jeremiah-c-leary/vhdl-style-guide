
from vsg.rules import multiline_constraint_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.signal_keyword, token.signal_declaration.semicolon])


class rule_017(Rule):
    '''
    This rule checks the structure of signal constraints.

    |configuring_multiline_constraint_rules_link|

    .. NOTE:: The indenting of multiline signal constraints is handled by the rule `signal_400 <signal_rules.html#signal-400>`_.

    **Violation**

    .. code-block:: vhdl

       signal sig_a : my_record(element1(7 downto 0), element2(3 downto 0));

    **Fix**

    .. code-block:: vhdl

       signal sig_a : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'signal', '017')
        self.lTokenPairs = lTokenPairs
