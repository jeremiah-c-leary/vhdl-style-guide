
from vsg.rules import token_case as Rule

from vsg.token import record_type_definition as token


class rule_500(Rule):
    '''
    This rule checks the proper case of the **record** keyword.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_record is RECORD
         a : std_logic;
         b : std_logic;
       end record t_record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '500', [token.record_keyword])
        self.groups.append('case::keyword')
