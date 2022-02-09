
from vsg.rules import blank_line_above_line_starting_with_token

from vsg.token import context_declaration as token


class rule_024(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **end** keyword.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

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
        blank_line_above_line_starting_with_token.__init__(self, 'context', '024', [token.end_keyword])
