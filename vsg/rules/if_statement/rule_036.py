
from vsg import token

from vsg.rules import move_token_left_to_next_non_whitespace_token

oToken = token.if_statement.then_keyword


class rule_036(move_token_left_to_next_non_whitespace_token):
    '''
    Checks code after the **elsif** keyword are on the same line as the **elsif** keyword.
    '''

    def __init__(self):
        move_token_left_to_next_non_whitespace_token.__init__(self, 'if', '036', oToken)
