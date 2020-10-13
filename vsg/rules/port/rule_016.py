
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import port_clause as token


class rule_016(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Moves port parameters to their own line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'port', '016', token.open_parenthesis)
        self.solution = 'Move port parameter to the next line.'
