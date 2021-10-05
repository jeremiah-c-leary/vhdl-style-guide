
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token

from vsg.token import procedure_specification as token


class rule_011(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token):
    '''
    Moves procedure parameters to their own line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token.__init__(self, 'procedure', '011', token.open_parenthesis, token.close_parenthesis)
        self.solution = 'Move procedure parameter to the next line.'
