
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_010(split_line_at_token):
    '''
    Moves the *begin* keyword to it's own line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'process', '010', lTokens)
        self.solution = 'Closing parenthesis must be on a line by itself.'
