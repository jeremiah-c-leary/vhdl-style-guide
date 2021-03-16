
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.use_clause.keyword, token.use_clause.selected_name])


class rule_006(single_space_between_token_pairs):
    '''
    Checks for a single space between the use keyword and the selected_name
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'library', '006', lTokens)
        self.solution = 'Ensure a single space between the *use* keyword and the selected_name.'
