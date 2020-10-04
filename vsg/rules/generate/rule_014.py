
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.case_generate_statement.label_colon, token.case_generate_statement.case_keyword])
lTokens.append([token.for_generate_statement.label_colon, token.for_generate_statement.for_keyword])
lTokens.append([token.if_generate_statement.label_colon, token.if_generate_statement.if_keyword])


class rule_014(single_space_between_token_pairs):
    '''
    Checks for a single space between the *end* keyword and the *generate* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generate', '014', lTokens)
        self.solution = 'Ensure a single space exists after the label colon.'
