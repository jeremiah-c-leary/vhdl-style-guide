
from vsg.rules.whitespace_between_tokens import Rule as Rule

from vsg.token import record_type_definition as token


class rule_100(Rule):
    '''
    This rule checks for a single space after the **end** keyword.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'record_type_definition', '100')
        self.left_token = token.end_keyword
        self.right_token = token.end_record_keyword
