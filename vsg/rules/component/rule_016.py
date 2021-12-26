
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_016(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines above the **end component** line.

    **Violation**

    .. code-block:: vhdl

           overflow : std_logic
         );



       end component fifo;

    **Fix**

    .. code-block:: vhdl

           overflow : std_logic
         );
       end component fifo;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'component', '016', lTokens)
        self.style = 'no_blank_line'
