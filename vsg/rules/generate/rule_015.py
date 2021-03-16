
from vsg import token

from vsg.rules import remove_carriage_returns_between_token_pairs

lTokens = []
lTokens.append([token.for_generate_statement.generate_label, token.for_generate_statement.for_keyword])
lTokens.append([token.if_generate_statement.generate_label, token.if_generate_statement.if_keyword])
lTokens.append([token.case_generate_statement.generate_label, token.case_generate_statement.case_keyword])


class rule_015(remove_carriage_returns_between_token_pairs):
    '''
    Checks label and generate keyword is on a single line.
    '''

    def __init__(self):
        remove_carriage_returns_between_token_pairs.__init__(self, 'generate', '015', lTokens)
        self.solution = 'Merge lines with generate label with *generate* keyword.'
