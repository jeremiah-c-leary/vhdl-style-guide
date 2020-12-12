
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import context_declaration as token


class rule_022(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks for indent on the end keyword.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'context', '022', token.context_simple_name, token.semicolon, token.end_keyword, token.semicolon, token.identifier)
        self.solution = 'context simple same'
