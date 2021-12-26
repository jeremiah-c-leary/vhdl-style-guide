
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import if_statement as token


class rule_033(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    This rule aligns consecutive comment only lines above the **else** keyword in if statements.
    These comments are used to describe what the elsif code is going to do.

    **Violation**

    .. code-block:: vhdl

           -- comment 1
     -- comment 2
        -- comment 3
       else
         rd_en <= '0';

    **Fix**

    .. code-block:: vhdl

       -- comment 1
       -- comment 2
       -- comment 3
       else
         rd_en <= '0';
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'if', '033', token.else_keyword)
        self.solution = 'Align comment with *else* keyword.'
