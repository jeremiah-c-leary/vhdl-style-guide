
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.generic_clause.generic_keyword, token.generic_clause.open_parenthesis])

class rule_003(single_space_between_token_pairs):
    '''
    Checks for a single space between the label and :.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generic', '003', lTokens)
        self.solution = 'Change spacing between "generic" and "(" to one space.'
