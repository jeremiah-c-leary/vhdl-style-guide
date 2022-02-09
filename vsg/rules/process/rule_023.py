
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_keyword)


class rule_023(blank_line_above_line_starting_with_token):
    '''
    This rule checks for a blank line above the **end process** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         wr_en <= '1';
       end process proc_a;

    **Fix**

    .. code-block:: vhdl

         wr_en <= '1';

       end process proc_a;
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'process', '023', lTokens)
