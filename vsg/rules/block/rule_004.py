
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_004(split_line_at_token):
    '''
    Moves begin keyword and code following it to the next line
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'block', '004', lTokens)
        self.solution = 'Move *begin* keyword and code after it to the next line'
