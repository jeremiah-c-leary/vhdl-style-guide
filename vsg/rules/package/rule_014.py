
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import package_declaration as token


class rule_014(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks the package name exists on the same line as the "end" and "package" keywords.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'package', '014', token.end_package_simple_name, token.semicolon, token.end_keyword, token.semicolon, token.identifier)
        self.solution = 'package name.'
