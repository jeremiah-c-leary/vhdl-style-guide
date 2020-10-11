
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_010(split_line_at_token):
    '''
    Moves library keyword and code to the right to it's own line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'library', '010', lTokens)
        self.solution = 'Move *library* to it\'s own line.'
