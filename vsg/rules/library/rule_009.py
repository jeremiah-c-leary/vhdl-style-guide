
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import use_clause as token


class rule_009(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    This rule checks alignment of comments above library use statements.

    **Violation**

    .. code-block:: vhdl

        library ieee;
        -- Use standard logic library
          use ieee.std_logic_1164.all;

    **Fix**

    .. code-block:: vhdl

        library ieee;
          -- Use standard logic library
          use ieee.std_logic_1164.all;
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'library', '009', token.keyword, bIncrement=True)
        self.solution = 'Align comment with *use* keyword.'
