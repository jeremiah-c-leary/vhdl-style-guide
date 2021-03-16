
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.end_keyword, token.process_statement.end_postponed_keyword])
lTokens.append([token.process_statement.end_keyword, token.process_statement.end_process_keyword])


class rule_007(single_space_between_token_pairs):
    '''
    Checks for a single space after the *end* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '007', lTokens)
        self.solution = 'Ensure a single space after the *end* keyword.'
