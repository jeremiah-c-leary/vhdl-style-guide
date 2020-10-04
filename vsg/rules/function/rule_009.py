
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import function_specification as token


class rule_009(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Moves function parameters to their own line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'function', '009', token.open_parenthesis)
        self.solution = 'Move function parameter to the next line.'
