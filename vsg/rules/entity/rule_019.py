
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import entity_declaration as token


class rule_019(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    This rule checks for the entity name in the **end entity** statement.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end entity;

    **Fix**

    .. code-block:: vhdl

       end entity entity_name;
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'entity', '019', token.entity_simple_name, token.semicolon, token.end_keyword, token.semicolon, token.identifier)
        self.subphase = 2
        self.solution = 'entity simple name'
        self.groups.append('structure::optional')
