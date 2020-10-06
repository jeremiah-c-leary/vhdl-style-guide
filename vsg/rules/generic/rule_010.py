
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_010(split_line_at_token):
    '''
    Moves code after the is keyword to the next line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'generic', '010', lTokens)
        self.solution = 'Closing parenthesis must be on a line by itself.'
