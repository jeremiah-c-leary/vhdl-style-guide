
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token as Rule

from vsg.token import case_generate_alternative as token


class rule_300(Rule):
    '''
    This rule aligns consecutive comment only lines above a **when** keyword in a case generate statement with the **when** keyword.

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
        Rule.__init__(self, 'case_generate_alternative', '300', token.when_keyword)
        self.solution = 'Align comment with *when* keyword.'
