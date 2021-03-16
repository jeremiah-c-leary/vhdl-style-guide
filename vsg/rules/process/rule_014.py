
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.process_keyword, token.process_statement.is_keyword])
lTokens.append([token.process_statement.close_parenthesis, token.process_statement.is_keyword])


class rule_014(single_space_between_token_pairs):
    '''
    Checks for a single space before the *is* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '014', lTokens)
        self.solution = 'Ensure a single space before the *is* keyword.'
