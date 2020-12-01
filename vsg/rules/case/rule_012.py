
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import case_statement_alternative as token

lTokens = []
lTokens.append(token.assignment)


class rule_012(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    Case rule 012 ensures code does not exist after the => operator.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'case', '012', lTokens)
        self.solution = 'Move code after the => to the next line.'
