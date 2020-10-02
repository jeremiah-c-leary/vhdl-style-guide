
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_005(split_line_at_token):
    '''
    Moves context reference keyword, and lines to the right, to the next line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'context_ref', '005', lTokens)
        self.solution = 'Move context and code after context to the next line'
