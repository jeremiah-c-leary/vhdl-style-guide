
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token

from vsg.token import entity_declaration as token


class rule_015(insert_token_right_of_token_if_it_does_not_exist_before_token):
    '''
    This rule checks for the keyword **entity** in the **end entity** statement.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end fifo;

       end;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;

       end entity;
    '''

    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'entity', '015', token.end_entity_keyword('entity'), token.end_keyword, token.semicolon)
        self.solution = '*entity* keyword'
