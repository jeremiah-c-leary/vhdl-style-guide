
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token

from vsg.token import package_declaration as token


class rule_007(insert_token_right_of_token_if_it_does_not_exist_before_token):
    '''
    Checks for *package* keyword in end package statement.
    '''

    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'package', '007', token.end_package_keyword('package'), token.end_keyword, token.semicolon)
        self.solution = '*package* keyword'
