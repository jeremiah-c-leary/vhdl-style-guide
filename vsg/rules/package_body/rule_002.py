
from vsg import parser

from vsg.rules import insert_tokens_right_of_token_if_it_does_not_exist_before_token

from vsg.token import package_body as token

lInsertTokens = []
lInsertTokens.append(token.end_package_keyword('package'))
lInsertTokens.append(parser.whitespace(' '))
lInsertTokens.append(token.end_body_keyword('body'))


class rule_002(insert_tokens_right_of_token_if_it_does_not_exist_before_token):
    '''
    Checks for *package* keyword in end package statement.
    '''

    def __init__(self):
        insert_tokens_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'package_body', '002', lInsertTokens, token.end_keyword, token.semicolon)
        self.solution = '*package body* keywords'
