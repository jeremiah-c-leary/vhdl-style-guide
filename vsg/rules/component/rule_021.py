
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token

from vsg.token import component_declaration as token


class rule_021(insert_token_right_of_token_if_it_does_not_exist_before_token):
    '''
    This rule inserts the optional **is** keyword if it does not exist.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       component my_component

       end my_component;

    **Fix**

    .. code-block:: vhdl

       component my_component is

       end my_component;
    '''
    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'component', '021', token.is_keyword('is'), token.identifier, token.semicolon)
        self.solution = '*is* keyword.'
        self.groups.append('structure::optional')
