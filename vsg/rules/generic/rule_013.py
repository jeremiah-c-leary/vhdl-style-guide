
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import generic_clause as token

lTokens = []
lTokens.append(token.open_parenthesis)


class rule_013(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Moves generic parameters to their own line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'generic', '013', lTokens)
        self.solution = 'Move generic parameter to the next line.'
