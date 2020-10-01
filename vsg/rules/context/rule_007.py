
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_007(split_line_at_token):
    '''
    Moves code after the is keyword to the next line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'context', '007', lTokens)
        self.solution = 'Move library and code after library to the next line'
