
from vsg import token

from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.adding_operator.plus)
lTokens.append(token.adding_operator.minus)
lTokens.append(token.multiplying_operator.star)
lTokens.append(token.multiplying_operator.slash)
lTokens.append(token.miscellaneous_operator.double_star)


class rule_011(n_spaces_before_and_after_tokens):
    '''
    Checks for spaces before and after math operators.
    '''

    def __init__(self):
        n_spaces_before_and_after_tokens.__init__(self, 'whitespace', '011', 1, lTokens, bNIsMinimum=True)
        self.solution = 'Ensure at least a single space before and after math operator.'
