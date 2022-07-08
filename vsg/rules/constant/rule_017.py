
from vsg.rules import multiline_constraint_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.constant_declaration.constant_keyword, token.constant_declaration.semicolon])


class rule_017(Rule):
    '''
    This rule checks the structure of constant constraints.

    |configuring_multiline_constraint_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant con_a : my_record(element1(7 downto 0), element2(3 downto 0));

    **Fix**

    .. code-block:: vhdl

       constant con_a : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'constant', '017')
        self.lTokenPairs = lTokenPairs
