
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import package_body as token

oInsertToken = token.end_package_simple_name

oLeftToken = token.semicolon

oStartToken = token.end_keyword
oEndToken = token.semicolon

oValueToken = token.package_simple_name


class rule_003(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks the package name exists on the same line as the "end" and "package" keywords.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'package_body', '003', oInsertToken, oLeftToken, oStartToken, oEndToken, oValueToken)
        self.solution = 'Add package name.'
