
from vsg.rules import token_indent as Rule

from vsg.token import record_type_definition as token


class rule_300(Rule):
    '''
    This rule checks the indent of the **record** keyword if it is on its own line.

    **Violation**

    .. code-block:: vhdl

       type t_record is
            record
         a : std_logic;
         b : std_logic;
       end record t_record;

    **Fix**

    .. code-block:: vhdl

       type t_record is
       record
         a : std_logic;
         b : std_logic;
       end record t_record;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '300', [token.record_keyword])
