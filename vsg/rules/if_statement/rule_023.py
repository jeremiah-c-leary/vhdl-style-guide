
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_023(split_line_at_token):
    '''
    Moves code after the *else* keyword to the next line.
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'if', '023', lTokens)
        self.solution = 'Move *elsif* keyword to it\'s own line.'
