
from vsg import token

from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.adding_operator.concat)


class rule_010(n_spaces_before_and_after_tokens):
    '''
    Whitespace rule 010 checks for spaces before semicolons
    '''

    def __init__(self):
        n_spaces_before_and_after_tokens.__init__(self, 'whitespace', '010', 1, lTokens)
        self.solution = 'Ensure a single space before and after concat operator.'
