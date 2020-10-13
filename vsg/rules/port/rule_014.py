
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.port_clause.close_parenthesis)


class rule_014(split_line_at_token):
    '''
    Moves the closing parenthesis to it's own line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'port', '014', lTokens)
        self.solution = 'Closing parenthesis must be on a line by itself.'
