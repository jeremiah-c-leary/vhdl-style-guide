
from vsg import parser

from vsg.rules import n_spaces_after_tokens

lTokens = []
lTokens.append(parser.comma)


class rule_007(n_spaces_after_tokens):
    '''
    Checks for spaces after a comma.
    '''

    def __init__(self):
        n_spaces_after_tokens.__init__(self, 'whitespace', '007', 1, lTokens, bNIsMinimum=True)
        self.solution = 'Add a space after comma.'
