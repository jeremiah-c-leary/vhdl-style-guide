
from vsg import token

from vsg.rules import move_token_left_to_next_non_whitespace_token

oToken = token.if_statement.then_keyword


class rule_036(move_token_left_to_next_non_whitespace_token):
    '''
    This rule checks the **then** keyword is not on a line by itself.

    **Violation**

    .. code-block:: vhdl

       if a = '1'
         then

    **Fix**

    .. code-block:: vhdl

       if a = '1' then
    '''

    def __init__(self):
        move_token_left_to_next_non_whitespace_token.__init__(self, 'if', '036', oToken)
