
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import process_statement as token


class rule_018(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks the process name exists on the same line as the "end" and "process" keywords.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'process', '018', token.end_process_label, token.semicolon, token.end_keyword, token.semicolon, token.process_label)
        self.solution = 'Add a label for the "end process".'
        self.subphase = 2
