
from vsg import token

from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.logical_operator.logical_operator)


class rule_013(n_spaces_before_and_after_tokens):
    '''
    Whitespace rule 013 checks for spaces before semicolons
    '''

    def __init__(self):
        n_spaces_before_and_after_tokens.__init__(self, 'whitespace', '013', 1, lTokens, bNIsMinimum=True)
        self.solution = 'Ensure a single space before and after concat operator.'
