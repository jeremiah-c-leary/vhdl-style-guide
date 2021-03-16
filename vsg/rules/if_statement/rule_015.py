
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.if_statement.end_keyword, token.if_statement.end_if_keyword])


class rule_015(single_space_between_token_pairs):
    '''
    Checks there is a single space between the if keyword and the (.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'if', '015', lTokens)
        self.solution = 'Ensure only a single space exists between the *end* and *if* keywords.'
