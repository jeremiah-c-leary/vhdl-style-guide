
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule

from vsg.token import record_type_definition as token
from vsg.token import full_type_declaration as ft_token

oInsertToken = token.record_type_simple_name
oAnchorToken = ft_token.semicolon
oLeftToken = token.end_record_keyword
oRightToken = ft_token.semicolon
oValueToken = ft_token.identifier


class rule_005(Rule):
    '''
    This rule checks for the optional simple name in the **end record** statement.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '005', oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.subphase = 1
        self.solution = 'record type simple name'
        self.groups.append('structure::optional')
