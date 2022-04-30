
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment as Rule

from vsg.token import record_type_definition as token

lTokens = []
lTokens.append(token.record_keyword)


class rule_002(Rule):
    '''
    This rule checks for code after the **record** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record a : std_logic;
         b : std_logic;
       end record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '002', lTokens)
        self.solution = 'Move code after the begin to the next line.'
