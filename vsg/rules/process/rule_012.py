
from vsg.rules import insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token

from vsg.token import process_statement as token

oInsertToken = token.is_keyword('is')

lRightTokens = []
lRightTokens.append(token.process_keyword)
lRightTokens.append(token.close_parenthesis)

oBeforeToken = token.begin_keyword


class rule_012(insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token):
    '''
    Checks for the existance of the "is" keyword.
    '''

    def __init__(self):
        insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token.__init__(self, 'process', '012', oInsertToken, lRightTokens, oBeforeToken)
        self.solution = '*is* keyword'
