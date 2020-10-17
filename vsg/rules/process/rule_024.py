
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.process_label, token.process_statement.label_colon])


class rule_024(single_space_between_token_pairs):
    '''
    Checks for a single space before the *is* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '024', lTokens)
        self.solution = 'Ensure a single space exists between process label and :.'
