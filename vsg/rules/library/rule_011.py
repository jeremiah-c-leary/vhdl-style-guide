
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_011(split_line_at_token):
    '''
    Moves use keyword and code to the right to it's own line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'library', '011', lTokens)
        self.solution = 'Move *use* to it\'s own line.'
