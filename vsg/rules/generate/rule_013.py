
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.case_generate_statement.end_generate_keyword, token.case_generate_statement.end_generate_label])
lTokens.append([token.for_generate_statement.end_generate_keyword, token.for_generate_statement.end_generate_label])
lTokens.append([token.if_generate_statement.end_generate_keyword, token.if_generate_statement.end_generate_label])


class rule_013(single_space_between_token_pairs):
    '''
    Checks for a single space between the *end* keyword and the *generate* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generate', '013', lTokens)
        self.solution = 'Ensure there is only one space between the *generate* keyword and the label.'
