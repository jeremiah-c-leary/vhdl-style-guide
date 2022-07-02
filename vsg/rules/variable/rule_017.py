
from vsg.rules import multiline_constraint_structure as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.variable_declaration.variable_keyword, token.variable_declaration.semicolon])


class rule_017(Rule):
    '''
    This rule checks the structure of variable constraints.

    |configuring_multiline_constraint_rules_link|

    .. NOTE:: The indenting of multiline variable constraints is handled by the rule `variable_400 <variable_rules.html#variable-400>`_.

    **Violation**

    .. code-block:: vhdl

       variable v_element : my_record(element1(7 downto 0), element2(3 downto 0));

    **Fix**

    .. code-block:: vhdl

       variable v_element : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'variable', '017')
        self.lTokenPairs = lTokenPairs
