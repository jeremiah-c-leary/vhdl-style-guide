
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens

from vsg import token


class rule_013(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens):
    '''
    Checks for multiple port terms on a single line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens.__init__(self, 'port', '013', [token.interface_list.semicolon], token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.solution = 'Move multiple ports to their own lines.'
