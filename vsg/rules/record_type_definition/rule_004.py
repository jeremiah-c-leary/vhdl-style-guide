
from vsg.rules import move_token_next_to_another_token as Rule

from vsg.token import record_type_definition as token


class rule_004(Rule):
    '''
    This rule checks the **is** keyword is on the same line as the **record** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end
       record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record
       ;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '004', token.end_keyword, token.end_record_keyword)
        self.subphase = 1
        self.solution = 'Move *record* next to *end* keyword'
