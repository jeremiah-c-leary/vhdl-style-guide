
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import case_statement_alternative as token


class rule_021(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    This rule aligns consecutive comment only lines above a **when** keyword in a case statement with the **when** keyword.

    **Violation**

    .. code-block:: vhdl

           -- comment 1
     -- comment 2
        -- comment 3
       when wr_en =>
         rd_en <= '0';

    **Fix**

    .. code-block:: vhdl

       -- comment 1
       -- comment 2
       -- comment 3
       when wr_en =>
         rd_en <= '0';
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'case', '021', token.when_keyword)
        self.solution = 'Align comment with *when* keyword.'
