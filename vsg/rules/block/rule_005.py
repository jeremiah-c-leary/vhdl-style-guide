
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import block_statement as token

lTokens = []
lTokens.append(token.begin_keyword)


class rule_005(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Ensures code does not exist after the begin keyword on the same line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'block', '005', lTokens)
        self.solution = 'Move code after the begin to the next line.'
