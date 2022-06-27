
from vsg.rules.whitespace_between_tokens import Rule as Rule

from vsg.token import record_type_definition as token


class rule_101(Rule):
    '''
    This rule checks for a single space before the simple name.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'record_type_definition', '101')
        self.left_token = token.end_record_keyword
        self.right_token = token.record_type_simple_name
