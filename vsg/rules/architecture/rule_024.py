
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import architecture_body as token


class rule_024(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    This rule checks for the architecture name in the **end architecture** statement.
    It is clearer to the reader to state which architecture the end statement is closing.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end architecture;

    **Fix**

    .. code-block:: vhdl

       end architecture architecture_name;
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'architecture', '024', token.architecture_simple_name, token.semicolon, token.end_keyword, token.semicolon, token.identifier)
        self.solution = 'architecture simple name'
        self.groups.append('structure::optional')
