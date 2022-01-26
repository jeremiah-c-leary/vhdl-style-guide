
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import context_declaration as token


class rule_027(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    This rule ensures a single blank line before the **end** keword.

    **Violation**

    .. code-block:: vhdl

         use ieee.std_logic_1164.all;



       end context;

    **Fix**

    .. code-block:: vhdl

         use ieee.std_logic_1164.all;

       end context;
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'context', '027', [token.end_keyword])
