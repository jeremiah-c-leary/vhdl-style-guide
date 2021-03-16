
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import if_statement as token

lTokens = []
lTokens.append(token.else_keyword)


class rule_022(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Checks for code after the "else" keyword.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'if', '022', lTokens)
        self.solution = 'Move code after *else* keyword to the next line.'
