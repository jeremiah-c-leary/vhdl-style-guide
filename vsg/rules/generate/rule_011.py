
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import for_generate_statement as token


class rule_011(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks for generate_simple_name.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'generate', '011', token.end_generate_label, token.semicolon, token.end_keyword, token.semicolon, token.generate_label)
        self.solution = 'Add generate label'
