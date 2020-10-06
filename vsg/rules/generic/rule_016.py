
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens

from vsg import token


class rule_016(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens):
    '''
    Generic rule 016 checks for multiple generic terms on a single line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens.__init__(self, 'generic', '016', [token.interface_list.semicolon], token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis)
        self.solution = 'Move multiple generics to their own lines.'
