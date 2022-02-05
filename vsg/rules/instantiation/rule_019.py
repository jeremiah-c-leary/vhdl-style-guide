
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.semicolon)


class rule_019(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the end of the instantiation declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
       U_RAM : RAM

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );

       U_RAM : RAM
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'instantiation', '019', lTokens)
