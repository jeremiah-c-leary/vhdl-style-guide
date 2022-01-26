
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_016(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines above the **end entity** keywords.

    **Violation**

    .. code-block:: vhdl

           wr_en : in    std_logic;
           rd_en : in    std_logic
         );


       end entity fifo;


    **Fix**

    .. code-block:: vhdl

           wr_en : in    std_logic;
           rd_en : in    std_logic
         );
       end entity fifo;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'entity', '016', lTokens)
        self.style = 'no_blank_line'
