
from vsg.rules import move_token_next_to_another_token as Rule

from vsg.token import record_type_definition as token


class rule_006(Rule):
    '''
    This rule checks the optional simple name is on the same line as the **record** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record
       t_record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record
       ;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '006', token.end_record_keyword, token.record_type_simple_name)
        self.subphase = 2
        self.solution = 'Move simple name next to *record* keyword'
