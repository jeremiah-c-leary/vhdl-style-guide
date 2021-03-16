
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.label_colon, token.process_statement.process_keyword])


class rule_025(single_space_between_token_pairs):
    '''
    Checks for a single space after the label colon.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '025', lTokens)
        self.solution = 'Ensure a single space exists between the : and the *process* keyword.'
