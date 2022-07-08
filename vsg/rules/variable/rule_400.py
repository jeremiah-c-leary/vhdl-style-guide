
from vsg.rules import multiline_alignment_between_tokens as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.variable_declaration.variable_keyword, token.variable_declaration.semicolon])


class rule_400(Rule):
    '''
    This rule checks alignment of multiline constraints in variable declarations.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable v_element : my_record(
                element1(7 downto 0),
       element2(3 downto 0)
               );

    **Fix**

    .. code-block:: vhdl

       variable v_element : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'variable', '400', lTokenPairs)
        self.phase = 5
        self.subphase = 3
        self.bIgnoreStartParen = True
