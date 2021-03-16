
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.case_generate_statement.end_keyword, token.case_generate_statement.end_generate_keyword])
lTokens.append([token.for_generate_statement.end_keyword, token.for_generate_statement.end_generate_keyword])
lTokens.append([token.if_generate_statement.end_keyword, token.if_generate_statement.end_generate_keyword])


class rule_008(single_space_between_token_pairs):
    '''
    Checks for a single space between the *end* keyword and the *generate* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generate', '008', lTokens)
        self.solution = 'Ensure there is only one space between the *end* and *generate* keywords.'
