
from vsg.rules import blank_line_below_line_ending_with_token as Rule

from vsg.token import record_type_definition as token


class rule_200(Rule):
    '''
    This rule checks for blank lines below the **record** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       type t_record is record

         a : std_logic;
         b : std_logic;
       end record    t_record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '200', [token.record_keyword])
        self.style = 'no_blank_line'
