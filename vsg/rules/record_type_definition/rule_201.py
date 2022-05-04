
from vsg.rules import previous_line as Rule

from vsg.token import record_type_definition as token


class rule_201(Rule):
    '''
    This rule checks for blank lines above the **end** keyword.

    |configuring_previous_line_rules_link|

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
        Rule.__init__(self, 'record_type_definition', '201', [token.end_keyword])
        self.style = 'no_blank_line'
