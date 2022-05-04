
from vsg.rules import single_space_between_tokens as Rule

from vsg.token import record_type_definition as token


class rule_100(Rule):
    '''
    This rule checks for a single space after the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end         record t_record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    '''
    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '100', token.end_keyword, token.end_record_keyword)
        self.solution = 'Reduce spaces between *end* keyword and *record* keyword to a single space.'
