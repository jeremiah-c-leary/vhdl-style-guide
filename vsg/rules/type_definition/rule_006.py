
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.full_type_declaration.identifier, token.full_type_declaration.is_keyword])


class rule_006(single_space_between_token_pairs):
    '''
    Checks for a single space before the *is* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'type', '006', lTokens)
        self.solution = 'Ensure only a single space before the *is* keyword.'
