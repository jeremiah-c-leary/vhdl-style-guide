
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.semicolon)


class rule_011(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **end process** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       end process proc_a;
       wr_en <= wr_en;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;

       wr_en <= wr_en;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'process', '011', lTokens)
