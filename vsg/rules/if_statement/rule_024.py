
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import if_statement as token


class rule_024(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Moves code after the *then* keyword to the next line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'if', '024', token.then_keyword)
        self.solution = 'Move code after "then" keyword to the next line.'
