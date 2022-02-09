
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token

from vsg.token import context_declaration as token


class rule_021(insert_token_right_of_token_if_it_does_not_exist_before_token):
    '''
    This rule checks for the keyword **context** in the **end context** statement.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end c1;

       end;

    **Fix**

    .. code-block:: vhdl

       end context c1;

       end context;
    '''

    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'context', '021', token.end_context_keyword('context'), token.end_keyword, token.semicolon)
        self.solution = '*context* keyword'
        self.groups.append('structure::optional')
