
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token

from vsg.token import function_specification as token


class rule_009(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token):
    '''
    Moves function parameters to their own line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token.__init__(self, 'function', '009', token.open_parenthesis, token.close_parenthesis)
        self.solution = 'Move function parameter to the next line.'
